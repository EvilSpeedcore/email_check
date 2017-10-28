import re


def check_email(email):
    """Check email for correctness according to specified conditions.

    Args:
        :param email: Email

    Returns:
        :return: bool: True for success, False otherwise.
        
    """
    main_email_pattern = re.compile(r"""
                                ^                       # beginning of string 
                                ([a-z0-9._\-\"!,:]      # allowed characters in username 
                                {1,127})                # username character limit 
                                @                       # username divided from domain name with at sign
                                (?=[a-z0-9\-_.]         # allowed characters in domain name
                                {4,257}$)               # domain character limit
                                \b([a-zA-Z0-9\-_]+)\b   # allowed characters in domain part before dot
                                \b.\b                   # dot
                                ([a-zA-Z0-9\-_]+        #  allowed characters in domain name after dot
                                [^-])                   # tirer not allowed in the very beginning or end of domain name
                                $                       # end of string
""", re.VERBOSE)
    if re.search(main_email_pattern, email):
        additional_email_pattern_1 = re.compile(r"""
                                                    \.\.    # two dots in a row are not allowed in username 
                                                    """, re.VERBOSE)
        if not re.search(additional_email_pattern_1, email.split('@')[0]):
            additional_email_pattern_2 = re.compile(r"""
                                                (\")(.+)?([!,:])?(\")   # only paired quotes are allowed in username
                                                                        # !,: can be only between paired quotes
                                                """, re.VERBOSE)
            additional_email_pattern_3 = re.compile(r"""
                                                ^               # beginning of string
                                                [a-z0-9._\-]+   # allowed characters in username except paired quotes
                                                $               # end of string
""", re.VERBOSE)
            if re.search(additional_email_pattern_2, email.split("@")[0]) or re.search(additional_email_pattern_3,
                                                                                       email.split('@')[0]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


