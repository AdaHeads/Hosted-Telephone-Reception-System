all: use-cases protocol-overview wiki integration-tests

use-cases:
	for conversion in scripts/user_view_to_sequence_diagram \
	                  scripts/user_sequence_diagram_to_png \
	                  scripts/user_view_to_system_view \
	                  scripts/system_view_to_sequence_diagram \
	                  scripts/system_sequence_diagram_to_png \
	                  scripts/system_sequence_diagram_to_test_case; do for use_case in use-cases/*/*/user.md; do ./$${conversion} $${use_case}; done; done

protocol-overview: wikis
	./scripts/compose_protocol_overview

wiki: use-cases wikis
	for use_case in use-cases/*/name; do \
	   ./scripts/compose_use_case $${use_case}; \
	done

wikis:
	mkdir -p wikis
	for wiki in DatabaseServers \
	            Hosted-Telephone-Reception-System \
	            Call-Flow-Control; do \
	   ( cd wikis && if [ -d $${wiki}.wiki ]; then \
	                    cd $${wiki}.wiki && git pull; \
	                 else \
	                    git clone https://github.com/AdaHeads/$${wiki}.wiki.git; \
	                 fi ); \
	done

wiki-status: wikis
	for wiki in wikis/*.wiki; do \
	   ( cd $${wiki} && basename $$(pwd) .wiki && git status && echo ); \
	done

integration-tests: use-cases
	./scripts/copy_tests

clean:
	rm -f use-cases/*/*/*.orig
	rm -f use-cases/*/*/*.rej
	rm -f use-cases/*/*/*\~

distclean: clean
	rm -f use-cases/*/*/user.seq-diag
	rm -f use-cases/*/*/user.seq-diag.png
	rm -f use-cases/*/*/system.md
	rm -f use-cases/*/*/system.seq-diag
	rm -f use-cases/*/*/system.seq-diag.png
	rm -f use-cases/*/*/test.py
	rm -rf wikis

.PHONY: use-cases protocol-overview wiki wikis wiki-status integration-tests clean distclean

