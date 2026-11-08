
class PasswordRules:

    @staticmethod
    def get_rules(password):

        return [
            {
                "name": "Minimum 8 characters",
                "passed": len(password) >= 8
            },
            {
                "name": "Uppercase letter (A-Z)",
                "passed": any(c.isupper() for c in password)
            },
            {
                "name": "Lowercase letter (a-z)",
                "passed": any(c.islower() for c in password)
            },
            {
                "name": "Digit (0-9)",
                "passed": any(c.isdigit() for c in password)
            },
            {
                "name": "Special character",
                "passed": any(
                    not c.isalnum() and not c.isspace()
                    for c in password
                )
            }
        ]
