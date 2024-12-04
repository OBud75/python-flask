class Score:
    def __init__(self, id, person_id, score):
        self.id = id
        self.person_id = person_id
        self.score = score

    def __repr__(self):
        return f"<Score(id={self.id}, person_id={self.person_id}, score={self.score})>"
