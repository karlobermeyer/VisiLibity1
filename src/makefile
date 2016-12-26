#Phony target.
current_target: main


#Compiler flags
#CXXFLAGS = -O0 -Wall -ggdb
CXXFLAGS = -O2
#Linker flags
#LDFLAGS = -O0 -Wall -ggdb
LDFLAGS = -O2


#Modules
main.o: main.cpp visilibity.hpp
visilibity.o: visilibity.cpp visilibity.hpp


#Executables
main: main.o visilibity.o
	g++ -o main $(CXXFLAGS) main.o visilibity.o


clean:   
	rm main *~ *.o *.do *.db
	clear
	pwd
	ls
