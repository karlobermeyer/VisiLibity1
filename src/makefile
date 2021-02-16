#Phony target.
all: main test_shortest_path


#Compiler flags
#CXXFLAGS = -O0 -Wall -ggdb
CXXFLAGS = -O2
#Linker flags
#LDFLAGS = -O0 -Wall -ggdb
LDFLAGS = -O2


#Modules
main.o: main.cpp visilibity.hpp
test_shortest_path.o: test_shortest_path.cpp visilibity.hpp
visilibity.o: visilibity.cpp visilibity.hpp


#Executables
main: main.o visilibity.o
	g++ -o main $(CXXFLAGS) main.o visilibity.o

test_shortest_path: test_shortest_path.o visilibity.o
	g++ -o test_shortest_path $(CXXFLAGS) test_shortest_path.o visilibity.o

clean:   
	rm main *~ *.o *.do *.db test_shortest_path
	clear
	pwd
	ls
