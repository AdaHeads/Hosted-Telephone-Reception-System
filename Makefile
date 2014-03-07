all: use-cases

use-cases:
	for conversion in scripts/user_view_to_sequence_diagram \
	                  scripts/user_sequence_diagram_to_png \
	                  scripts/user_view_to_system_view \
	                  scripts/system_view_to_sequence_diagram \
	                  scripts/system_sequence_diagram_to_png \
	                  scripts/system_view_to_test_case; do for use_case in use-cases/*/*/user.md; do ./$${conversion} $${use_case}; done; done

wiki: use-cases
	for use_case in use-cases/*/name; do \
	   ./scripts/compose_use_case $${use_case}; \
	done

clean:
	rm -f use-cases/*/*/*.orig
	rm -f use-cases/*/*/*.rej

distclean: clean
	rm -f use-cases/*/*/user.seq-diag
	rm -f use-cases/*/*/user.seq-diag.png
	rm -f use-cases/*/*/system.md
	rm -f use-cases/*/*/system.seq-diag
	rm -f use-cases/*/*/system.seq-diag.png
	rm -f use-cases/*/*/test.py

.PHONY: use-cases clean distclean

