/*
 * This program will create a testable scenario based on user input for
 * generating the shortest path between two points in an environment and compare
 * that with expected results.
 *
 * Usage:
 * ./test_shortest_path <test environment file> <test path start/finish file>
 * <test results file>
 *
 * See README.md for information about the format of these files.
 */

#include "visilibity.hpp" //VisiLibity header file
#include <cmath>          //Puts math functions in std namespace
#include <cstdlib>        //Gives rand, srand, exit
#include <cstring>        //Gives C-string manipulation
#include <ctime>          //Gives Unix time
#include <fstream>        //File I/O
#include <iostream>       //std I/O
#include <sstream>        //Gives string streams
#include <string>         //Gives string class
#include <vector>         //std vectors
//#define NDEBUG           //Turns off assert.
#include <cassert>

// ASCII escape sequences for formatting terminal text.
std::string alert("\a");       // Beep
std::string normal("\x1b[0m"); // Designated fg color default bg color
std::string red("\x1b[31m");
std::string red_blink("\x1b[5;31m");
std::string black("\E[30;47m");
std::string green("\E[32m");
std::string yellow("\E[33;40m");
std::string blue("\E[34;47m");
std::string magenta("\x1b[35m");
std::string cyan("\E[36m");
std::string white_bold("\E[1;37;40m");
std::string clear_display("\E[2J");

void print_usage(const char *const self_name) {
  std::cout << self_name
            << " <test environment file> <test path start/stop file> <test "
               "results file>"
            << std::endl;
  std::cout
      << "\tSee README.md for information about the format of these files."
      << std::endl;
}

int main(int argc, char *argv[]) {

  // Check whether the user gave us the right number of parameters. If not, tell
  // them how to use our program.
  if (argc != 4) {
    print_usage(argv[0]);
    exit(1);
  }

  // Variables for the filenames specified on the command line.
  std::string test_environment_filename(argv[1]);
  std::string test_start_finish_filename(argv[2]);
  std::string test_results_filename(argv[3]);

  // Set the precision of the numbers that we will print to the screen for the
  // user to see.
  VisiLibity::Unit_Test::set_output_precision();
  // Seed the random number generator that we have to use throughout the code.
  VisiLibity::Unit_Test::seed_random();

  // Set geometric robustness constant
  //:WARNING:
  // may need to modify epsilon for Environments with greatly varying
  // scale of features
  double epsilon = 0.000000001;
  std::cout << "The robustness constant epsilon is set to " << epsilon
            << std::endl;

  // Load geometric environment model from file
  std::cout << "Loading test environment file ";
  // Print environment filename to screen
  std::cout << test_environment_filename << " . . . ";
  // Construct Environment object from file
  VisiLibity::Environment test_environment(test_environment_filename);
  std::cout << green << "OK" << normal << std::endl;

  // Load start/finish positions from file
  std::cout << "Loading test start/finish file ";
  // Print start/finish filename to screen
  std::cout << test_start_finish_filename << " . . . ";
  // Construct a Guards object from file
  VisiLibity::Guards test_start_finish(test_start_finish_filename);
  std::cout << green << "OK" << normal << std::endl;

  // Load the expected shortest path coordinates from file
  std::cout << "Loading expected results file ";
  // Print the expected shortest path coordinates filename to screen
  std::cout << test_results_filename << " . . . ";
  // Construct the Polyline of the expected shortest path from the file
  VisiLibity::Polyline expected_shortest_path(test_results_filename);
  std::cout << green << "OK" << normal << std::endl;

  // Satisfy the preconditions for visibility polygon calculation by snapping
  // the observers.
  test_start_finish.snap_to_boundary_of(test_environment, epsilon);
  test_start_finish.snap_to_vertices_of(test_environment, epsilon);

  // Check whether the parameters in the input files make a testable
  // scenario.
  assert(VisiLibity::Shortest_Path_Test::validate(test_environment, epsilon,
                                                  test_start_finish));
  std::cout
      << "Shortest path test parameters specified by input files are . . . "
      << green << "OK" << normal << std::endl;

  // Compute the shortest path between the two guards.
  VisiLibity::Polyline actual_shortest_path = test_environment.shortest_path(
      test_start_finish[0], test_start_finish[1], epsilon);

  // Print the actual and expected shortest path to help the user debug
  // failures.
  std::cout << "The (actual) shortest path is" << std::endl
            << magenta << actual_shortest_path << normal << std::endl;
  std::cout << "The (expected) shortest path is" << std::endl
            << magenta << expected_shortest_path << normal << std::endl;

  // If the actual and expected shortest paths match, then print that the test
  // passed and return 0 (no error). Otherwise, Alert the user of failure and
  // return 1 (error).
  if (actual_shortest_path == expected_shortest_path) {
    std::cout << green << "Passed" << normal << std::endl;
    return 0;
  } else {
    std::cout << red << "Failed" << normal << std::endl;
    return 1;
  }
}
