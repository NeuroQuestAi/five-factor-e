"""Reverses scores for certain questions from the IPIP-120, IPIP-300 and Custom Items."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
__status__ = "production"

from ipipneo.utility import reverse_scored

IPIP_NEO_ITEMS_REVERSED_120 = [
    9,
    19,
    24,
    30,
    39,
    40,
    48,
    49,
    51,
    53,
    54,
    60,
    62,
    67,
    68,
    69,
    70,
    73,
    74,
    75,
    78,
    79,
    80,
    81,
    83,
    84,
    85,
    88,
    89,
    90,
    92,
    94,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    113,
    114,
    115,
    116,
    118,
    119,
    120,
]

IPIP_NEO_ITEMS_REVERSED_300 = [
    69,
    99,
    109,
    118,
    120,
    129,
    138,
    139,
    144,
    148,
    149,
    150,
    151,
    152,
    156,
    157,
    158,
    159,
    160,
    162,
    163,
    164,
    165,
    167,
    168,
    169,
    171,
    173,
    174,
    175,
    176,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    185,
    186,
    187,
    188,
    189,
    190,
    192,
    193,
    194,
    195,
    196,
    197,
    198,
    199,
    201,
    203,
    204,
    205,
    206,
    208,
    209,
    210,
    211,
    212,
    213,
    214,
    215,
    216,
    217,
    218,
    219,
    220,
    221,
    222,
    223,
    224,
    225,
    226,
    227,
    228,
    229,
    230,
    231,
    233,
    234,
    235,
    236,
    238,
    239,
    240,
    241,
    242,
    243,
    244,
    245,
    246,
    247,
    248,
    249,
    250,
    251,
    252,
    253,
    254,
    255,
    256,
    257,
    258,
    259,
    260,
    261,
    262,
    263,
    264,
    265,
    266,
    267,
    268,
    269,
    270,
    271,
    272,
    273,
    274,
    275,
    276,
    277,
    278,
    279,
    280,
    281,
    282,
    283,
    284,
    285,
    286,
    287,
    288,
    289,
    290,
    291,
    292,
    293,
    294,
    295,
    296,
    297,
    298,
    299,
    300,
]


class ReverseScoredCustom:
    """Reverse scored for Tests."""

    def __new__(self, answers: dict) -> dict | BaseException | AssertionError:
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
            raise ValueError("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_select) was not found!")

        if not any("reverse_scored" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (reverse_scored) was not found!")

        def is_reversed_custom(x: dict) -> dict:
            x["id_select"] = (
                reverse_scored(select=x["id_select"])
                if x.get("reverse_scored") == 1
                else x["id_select"]
            )
            return x

        return {
            "answers": [is_reversed_custom(x=x) for x in answers.get("answers", [])]
        }


class ReverseScored120:
    """Reverse scored for IPIP-120."""

    def __new__(self, answers: dict) -> dict | BaseException | AssertionError:
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
            raise ValueError("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_select) was not found!")

        assert (
            len(list(IPIP_NEO_ITEMS_REVERSED_120)) == 55
        ), "The number of reverse items should be 55!"

        def is_reversed_120(x: int, y: int) -> int:
            for i in IPIP_NEO_ITEMS_REVERSED_120:
                if x == i:
                    return reverse_scored(select=y)
            return y

        update = map(
            lambda x: x.__setitem__(
                "id_select", is_reversed_120(x["id_question"], x["id_select"])
            ),
            answers.get("answers"),
        )
        assert len(list(update)) == 120, "The update number should be 120!"

        return answers or {}


class ReverseScored300:
    """Reverse scored for IPIP-300."""

    def __new__(self, answers: dict) -> dict | BaseException | AssertionError:
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
            raise ValueError("The key named (answers) was not found!")

        if not any("id_question" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_question) was not found!")

        if not any("id_select" in x for x in answers.get("answers", [])):
            raise ValueError("The key named (id_select) was not found!")

        assert (
            len(list(IPIP_NEO_ITEMS_REVERSED_300)) == 148
        ), "The number of reverse items should be 148!"

        def is_reversed_300(x: int, y: int) -> int:
            for i in IPIP_NEO_ITEMS_REVERSED_300:
                if x == i:
                    return reverse_scored(select=y)
            return y

        update = map(
            lambda x: x.__setitem__(
                "id_select", is_reversed_300(x["id_question"], x["id_select"])
            ),
            answers.get("answers"),
        )
        assert len(list(update)) == 300, "The update number should be 300!"

        return answers or {}
