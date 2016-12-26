# Generates VisiLibity webpage, download package file, and web documentation.

# \Get today's date in two different formats
TODAY =`date "+%Y_%m_%d" | tail -c 11`
TODAY2 =`date "+%Y:%m:%d" | tail -c 11`

# Abbreviations
S = "./src"

public: clean
	@echo "(1) Generate doxygen documentation and place in ./doxygen_html"
	@doxygen VisiLibity.Doxyfile
	@echo "(2) Generate gzip'd tar ball of VisiLibity files"
	@tar czvf "./VisiLibity."${TODAY}".tgz" \
	README.md COPYING COPYING.LESSER \
	$S/visilibity.hpp $S/visilibity.cpp $S/main.cpp $S/makefile \
	$S/example1.environment $S/example2.environment \
	$S/example1.guards \
	$S/visibility_polygon.cpp \
	$S/in_environment.cpp \
	$S/shortest_path.cpp \
	$S/visibility_graph.cpp \
	$S/visibility_polygon_demo.m \
	$S/shortest_path_demo.m \
	$S/visibility_graph_demo.m \
	$S/read_vertices_from_file.m
	#to view contents use tar tzvf ...
	#to extract use tar xzvf ...
	@echo "(3) Update all dates in ./index.html to today's date"
	sed "s/[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9]/${TODAY}/g;s/[0-9][0-9][0-9][0-9]:[0-9][0-9]:[0-9][0-9]/${TODAY2}/g" \
	./index.html > ./index_temp.html
	cp ./index_temp.html ./index.html
	rm ./index_temp.html
	@echo "(4) Set permissions for public access"
	./setperms.sh
	@clear
	@echo
	@echo "Files in . : "
	@echo
	@ls -Gfl .
	@echo
	@echo "where ./VisiLibity."${TODAY}".tgz contains"
	@echo
	@tar tzvf "./VisiLibity."${TODAY}".tgz"
	git add "./VisiLibity."${TODAY}".tgz"
	git add doxygen_html

clean:
	if [ -a ./VisiLibity*.tgz ] ; \
	then \
		git rm ./VisiLibity*.tgz ; \
	fi;
	rm -rf *~ ./VisiLibity*.tgz ./doxygen_html
	clear
	pwd
	ls -Gfl

# Abbreviations note: $* stands for file name w/out extension, $@ w/extension.
