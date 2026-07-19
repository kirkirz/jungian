from jungian.models.mbti import from_mbti
from jungian.models.beebe import nemesis

t = from_mbti("INTP")
print(f"Nemesis of INTP: {nemesis(t)}")
