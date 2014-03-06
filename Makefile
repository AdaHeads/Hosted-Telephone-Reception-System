all: use-cases

use-cases:
	for conversion in scripts/user_view_to_sequence_diagram \
	                  scripts/user_sequence_diagram_to_png \
	                  scripts/user_view_to_system_view \
	                  scripts/system_view_to_sequence_diagram \
	                  scripts/system_sequence_diagram_to_png \
	                  scripts/system_view_to_test_case; do for use_case in use-cases/*/*/user.md; do ./$${conversion} $${use_case}; done; done

clean:
	rm -f use-cases/*/*/*.orig
	rm -f use-cases/*/*/*.rej

distclean: clean

.PHONY: use-cases clean distclean

