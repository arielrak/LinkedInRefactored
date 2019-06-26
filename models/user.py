from dataclasses import dataclass

@dataclass
class User:
    name: str = ""
    title: str = ""
    position: str = ""
    summary: str = ""
    skills: str = ""
    experience: str = ""
    education: str = ""

    # Completely arbitrary scoring metric
    def get_score(self):
        if len(self.skills) > 4:
            return self.skills[3]
        else:
            return 0