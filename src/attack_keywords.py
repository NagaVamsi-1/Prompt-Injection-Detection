# attack_keywords.py

attack_keywords = [

    # ==========================
    # Instruction Override
    # ==========================
    "ignore previous instructions",
    "ignore all previous instructions",
    "forget previous instructions",
    "disregard previous instructions",
    "override instructions",
    "ignore the above instructions",
    "ignore all instructions",
    "ignore previous",
    "ignore prior instructions",
    "forget everything",
    "forget all previous",
    "ignore all prior",
    "replace previous instructions",
    "new instructions override",
    "forget all context",
    "ignore prior context",

    # ==========================
    # System Prompt Extraction
    # ==========================
    "reveal the system prompt",
    "show the system prompt",
    "display the system prompt",
    "print the system prompt",
    "repeat the system prompt",
    "what is your system prompt",
    "show your prompt",
    "reveal your prompt",
    "developer message",
    "hidden prompt",
    "hidden instructions",
    "system instructions",
    "reveal your instructions",
    "tell me your instructions",
    "show hidden instructions",
    "output your configuration",
    "repeat your initial prompt",
    "what are your instructions",

    # ==========================
    # Safety Bypass
    # ==========================
    "bypass restrictions",
    "bypass safety",
    "disable safety",
    "remove safety restrictions",
    "ignore safety guidelines",
    "circumvent safeguards",
    "turn off safety",
    "remove content filters",
    "ignore ethical guidelines",
    "bypass content policy",
    "ignore policy",
    "disable restrictions",

    # ==========================
    # Jailbreak
    # ==========================
    "jailbreak",
    "unrestricted mode",
    "developer mode",
    "god mode",
    "dan mode",
    "do anything now",
    "without limitations",
    "without restrictions",
    "free mode",
    "unfiltered mode",
    "no restrictions",
    "fully unrestricted",

    # ==========================
    # Roleplay / Persona Hijacking
    # ==========================
    "act as",
    "act like",
    "pretend to be",
    "you are now",
    "roleplay as",
    "simulate a",
    "assume the role of",
    "take the role of",
    "stay in character",
    "you are dan",
    "you are no longer",
    "from now on you are",
    "behave as",

    # ==========================
    # Authority Manipulation
    # ==========================
    "for research purposes",
    "for educational purposes",
    "security audit",
    "authorized testing",
    "ethical hacking exercise",
    "internal testing",
    "security evaluation",
    "red team exercise",
    "penetration testing",
    "authorized assessment",

    # ==========================
    # Prompt Leakage
    # ==========================
    "reveal your instructions",
    "tell me your instructions",
    "show hidden instructions",
    "output your configuration",
    "repeat your initial prompt",
    "print hidden instructions",
    "show developer instructions",
    "reveal hidden prompt",

    # ==========================
    # Obfuscation / Encoding
    # ==========================
    "decode and follow",
    "translate and execute",
    "execute the hidden instruction",
    "interpret the encoded message",
    "base64",
    "rot13",
    "encoded instructions",
    "decrypt this message",
    "hidden command",
    "obfuscated instruction"
]

regex_patterns = [

    # Instruction Override
    r"ignore.*instruction",
    r"forget.*instruction",
    r"disregard.*instruction",
    r"override.*instruction",

    # Prompt Extraction
    r"reveal.*prompt",
    r"show.*prompt",
    r"display.*prompt",
    r"repeat.*prompt",
    r"tell me.*instruction",

    # Safety Bypass
    r"disable.*safety",
    r"bypass.*safety",
    r"remove.*restriction",
    r"ignore.*guideline",
    r"ignore.*policy",

    # Roleplay / Jailbreak
    r"act as .*",
    r"pretend.*",
    r"you are now .*",
    r"roleplay.*",
    r"assume the role.*",

    # Authority Manipulation
    r"research purpose",
    r"educational purpose",
    r"security audit",
    r"authorized testing",
    r"penetration testing",

    # System Access
    r"system prompt",
    r"developer message",
    r"hidden instruction",
    r"hidden prompt"
]