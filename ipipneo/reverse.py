"""Reverses scores for certain questions from the IPIP-120 and IPIP-300."""

__author__ = "Ederson Corbari"
__email__ = "e@neural7.io"
__copyright__ = "Copyright Neural7 2022, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "production"

from ipipneo.utility import reverse_scored


class ReverseScoredCustom:
    """Reverse scored for Tests."""

    def __new__(self, answers: dict) -> dict or BaseException or AssertionError:
        """
        Apply reverse scoring to items with key (reverse_scored=1).

        Used to test reverse scored questions! Reverse-scored items were recoded
        (1=5, 2=4, 4=2, 5=1) at the time the respondent completed the inventory,
        so values for these items can simply be added without recoding whenscale
        scores are computed.

        Example position: [1, 2, 3, 4, 5] to [5, 4, 3, 2, 1].

        Args:
            - answers: Dictionary with the list of answers.
        """
        assert isinstance(answers, dict), "The (answers) field must be a dict!"

        if "answers" not in answers:
            raise BaseException("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_select) was not found!")

        if not any("reverse_scored" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (reverse_scored) was not found!")

        def is_reversed(x: dict) -> dict:
            x["id_select"] = (
                reverse_scored(select=x["id_select"])
                if x.get("reverse_scored") == 1
                else x["id_select"]
            )
            return x

        return {"answers": [is_reversed(x=x) for x in answers.get("answers", [])]}


class ReverseScored120:
    """Reverse scored for IPIP-120."""

    def __new__(self, answers: dict) -> dict or BaseException or AssertionError:
        """
        Apply reverse scoring on certain items (IPIP-120).

        Reverse-scored items were recoded (1=5, 2=4, 4=2, 5=1) at the time the respondent
        completed the inventory, so values for these items can simply be added without
        recoding whenscale scores are computed.

        Example position: [1, 2, 3, 4, 5] to [5, 4, 3, 2, 1].

        Args:
            - answers: Dictionary with the list of answers.
        """
        assert isinstance(answers, dict), "The (answers) field must be a dict!"

        if "answers" not in answers:
            raise BaseException("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_select) was not found!")

        for i, x in enumerate(answers.get("answers", [])):
            if x.get("id_question", 0) == 9:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 19:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 24:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 30:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 39:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 40:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 48:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 49:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 51:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 53:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 54:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 60:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 62:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 67:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 68:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 69:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 70:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 73:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 74:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 75:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 78:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 79:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 80:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 81:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 83:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 84:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 85:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 88:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 89:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 90:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 92:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 94:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 96:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 97:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 98:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 99:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 100:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 101:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 102:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 103:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 104:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 105:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 106:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 107:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 108:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 109:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 110:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 111:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 113:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 114:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 115:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 116:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 118:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 119:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 120:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )

        return answers or {}


class ReverseScored300:
    """Reverse scored for IPIP-300."""

    def __new__(self, answers: dict) -> dict or BaseException or AssertionError:
        """
        Apply reverse scoring on certain items (IPIP-300).

        Reverse-scored items were recoded (1=5, 2=4, 4=2, 5=1) at the time the respondent
        completed the inventory, so values for these items can simply be added without
        recoding whenscale scores are computed.

        Example position: [1, 2, 3, 4, 5] to [5, 4, 3, 2, 1].

        Args:
            - answers: Dictionary with the list of answers.
        """
        assert isinstance(answers, dict), "The (answers) field must be a dict!"

        if "answers" not in answers:
            raise BaseException("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise BaseException("The key named (id_select) was not found!")

        for i, x in enumerate(answers.get("answers", [])):
            if x.get("id_question", 0) == 69:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 99:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 109:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 118:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 120:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 129:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 138:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 139:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 144:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 148:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 149:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 150:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 151:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 152:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 156:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 157:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 158:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 159:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 160:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 162:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 163:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 164:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 165:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 167:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 168:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 169:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 171:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 173:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 174:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 175:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 176:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 178:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 179:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 180:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 181:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 182:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 183:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 184:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 185:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 186:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 187:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 188:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 189:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 190:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 192:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 193:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 194:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 195:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 196:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 197:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 198:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 199:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 201:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 203:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 204:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 205:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 206:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 208:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 209:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 210:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 211:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 212:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 213:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 214:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 215:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 216:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 217:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 218:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 219:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 220:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 221:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 222:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 223:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 224:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 225:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 226:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 227:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 228:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 229:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 230:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 231:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 233:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 234:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 235:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 236:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 238:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 239:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 240:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 241:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 242:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 243:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 244:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 245:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 246:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 247:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 248:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 249:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 250:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 251:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 253:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 252:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 254:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 255:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 256:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 257:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 259:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 258:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 260:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 261:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 262:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 263:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 264:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 265:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 266:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 267:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 268:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 269:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 270:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 271:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 272:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 273:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 274:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 275:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 276:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 277:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 278:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 279:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 281:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 280:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 282:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 283:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 284:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 285:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 286:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 287:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 288:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 289:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 290:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 291:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 292:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 294:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 293:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 295:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 296:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 297:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 298:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 299:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )
            if x.get("id_question", 0) == 300:
                answers["answers"][i]["id_select"] = reverse_scored(
                    select=x.get("id_select", 0)
                )

        return answers or {}
