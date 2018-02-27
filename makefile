# Generates VisiLibity webpage, including Doxygen documentation.

public: clean
	@echo "Generating doxygen documentation and placing in ./doxygen_html ."
	@doxygen VisiLibity.Doxyfile
	./setperms.sh
	@clear
	@echo
	@echo "Files in . : "
	@echo
	@ls -Gfl .
	@echo
	git add doxygen_html
	git commit -m "Generate webpage."
	git push -f --set-upstream origin gh-pages

clean:
	rm -rf *~ ./doxygen_html
	clear
	pwd
	ls -Gfl

# Abbreviations note: $* stands for file name w/out extension, $@ w/extension.
