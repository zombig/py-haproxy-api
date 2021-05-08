# frozen_string_literal: true

################################################################################
# Style file for markdownlint.
#
# https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md
#
# This file is referenced by the project `.mdlrc`.
################################################################################

#===============================================================================
# Start with all built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
all

#===============================================================================
# Override default parameters for some built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/creating_styles.md#parameters

exclude_rule 'MD004' # Unordered list style
exclude_rule 'MD007' # Unordered list indentation
exclude_rule 'MD029' # Ordered list item prefix
exclude_rule 'MD013' # Line length
