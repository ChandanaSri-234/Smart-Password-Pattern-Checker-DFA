
class PasswordDFA:

    MIN_LENGTH = 8

    PROHIBITED_PATTERNS = [
        "password",
        "123456",
        "qwerty",
        "admin"
    ]

    def __init__(self):
        self.max_pattern_length = max(
            len(p) for p in self.PROHIBITED_PATTERNS
        )

    def initial_state(self):
        return (0, False, False, False, False, "", False)

    def state_description(self, state):
        if state == "REJECT":
            return "Prohibited pattern detected"

        length, upper, lower, digit, special, suffix, rejected = state

        return (
            f"Length: {length}/8 | "
            f"Uppercase: {upper} | "
            f"Lowercase: {lower} | "
            f"Digit: {digit} | "
            f"Special: {special}"
        )

    def transition(self, state, char):

        if state == "REJECT":
            return "REJECT"

        length, upper, lower, digit, special, suffix, rejected = state

        length = min(length + 1, self.MIN_LENGTH)

        upper = upper or char.isupper()
        lower = lower or char.islower()
        digit = digit or char.isdigit()

        special = special or (
            not char.isalnum() and not char.isspace()
        )

        suffix = (
            suffix + char.lower()
        )[-self.max_pattern_length:]

        for pattern in self.PROHIBITED_PATTERNS:
            if pattern in suffix:
                return "REJECT"

        return (
            length,
            upper,
            lower,
            digit,
            special,
            suffix,
            False
        )

    def validate(self, password):

        state = self.initial_state()

        state_names = {state: "q0"}
        transitions = []

        def get_state_name(current_state):

            if current_state == "REJECT":
                return "qReject"

            if current_state not in state_names:
                state_names[current_state] = (
                    f"q{len(state_names)}"
                )

            return state_names[current_state]

        initial_name = get_state_name(state)

        for char in password:

            current_name = get_state_name(state)

            next_state = self.transition(state, char)

            next_name = get_state_name(next_state)

            transitions.append({
                "from": current_name,
                "to": next_name,
                "symbol": char,
                "description": self.state_description(next_state)
            })

            state = next_state

        if state == "REJECT":

            valid = False
            violations = [
                "Prohibited password pattern detected"
            ]

        else:

            length, upper, lower, digit, special, suffix, rejected = state

            valid = (
                length >= self.MIN_LENGTH
                and upper
                and lower
                and digit
                and special
            )

            violations = []

            if length < self.MIN_LENGTH:
                violations.append("Minimum 8 characters required")

            if not upper:
                violations.append("Uppercase letter missing")

            if not lower:
                violations.append("Lowercase letter missing")

            if not digit:
                violations.append("Digit missing")

            if not special:
                violations.append("Special character missing")

        final_state = "qAccept" if valid else "qReject"

        transitions.append({
            "from": get_state_name(state),
            "to": final_state,
            "symbol": "END",
            "description": "Final password classification"
        })

        return {
            "valid": valid,
            "violations": violations,
            "transitions": transitions,
            "final_state": final_state,
            "analysis": {
                "length": len(password),
                "uppercase": (
                    any(c.isupper() for c in password)
                ),
                "lowercase": (
                    any(c.islower() for c in password)
                ),
                "digit": (
                    any(c.isdigit() for c in password)
                ),
                "special": (
                    any(
                        not c.isalnum() and not c.isspace()
                        for c in password
                    )
                )
            }
        }
