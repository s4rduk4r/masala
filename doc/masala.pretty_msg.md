# masala.pretty_msg
Print colored info, warnings, error messages
---
- [pretty_msg.print_msg](#masala_pretty_msg_print_msg)
- [pretty_msg.print_warn](#masala_pretty_msg_print_warn)
- [pretty_msg.print_error](#masala_pretty_msg_print_error)

---
## <a id="masala_pretty_msg_print_msg">pretty_msg.print_msg(msg)</a>
Normal info message. Text color is blue

**Parameters:**   **msg (str)**

    Info text

**Returns:** None

---
## <a id="masala_pretty_msg_print_warn">pretty_msg.print_warn(msg)</a>
Warning message. Text color is magenta

**Parameters:** **msg (str)**

    Warning text

**Returns:** None

---
## <a id="masala_pretty_msg_print_error">pretty_msg.print_error(error)</a>
Exception and other critical message. Text color is red

**Parameters:** **error (Exception)**
    
    Exception to pass as a function argument

**Returns:** None
