__all__ = ["asserts", "pretty_msg"]

__version__ = "0.0.1"

import masala.asserts
import masala.pretty_msg

assert_step = masala.asserts.assert_step
print_error = masala.pretty_msg.print_error
print_msg = masala.pretty_msg.print_msg
print_warn = masala.pretty_msg.print_warn

import masala.preprocessing.dataframe
open_dataset = masala.preprocessing.dataframe.open_dataset
na_counts_and_props = masala.preprocessing.dataframe.na_counts_and_props