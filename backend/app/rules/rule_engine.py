from app.rules.legal_rules import LEGAL_RULES

class RuleEngine:
    def __init__(self):
        self.rules = LEGAL_RULES
    
    def get_rules(self):
        return self.rules
    
    