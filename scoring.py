"""Question bank, psychological constructs, and scoring functions for the Big Five assessment."""

TRAITS = [
    "Openness",
    "Conscientiousness",
    "Extraversion",
    "Agreeableness",
    "Neuroticism",
]

TRAIT_DETAILS = {
    "Openness": {
        "icon": "🔮",
        "color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #8B5CF6 0%, #D946EF 100%)",
        "alias": "Curiosity & Imagination",
        "subtitle": "Intellectual appetite, artistic sensibility, and hunger for novelty.",
    },
    "Conscientiousness": {
        "icon": "🎯",
        "color": "#10B981",
        "gradient": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "alias": "Drive & Organization",
        "subtitle": "Goal persistence, reliability, methodical discipline, and attention to detail.",
    },
    "Extraversion": {
        "icon": "⚡",
        "color": "#F59E0B",
        "gradient": "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
        "alias": "Energy & Social Magnetism",
        "subtitle": "Enthusiasm, assertiveness, group social energy, and spontaneous expression.",
    },
    "Agreeableness": {
        "icon": "🤝",
        "color": "#06B6D4",
        "gradient": "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
        "alias": "Empathy & Harmony",
        "subtitle": "Compassion, collaborative spirit, warmth, and faith in human goodness.",
    },
    "Neuroticism": {
        "icon": "🌊",
        "color": "#F43F5E",
        "gradient": "linear-gradient(135deg, #F43F5E 0%, #FB7185 100%)",
        "alias": "Emotional Reactivity",
        "subtitle": "Sensitivity to stressors, emotional depth, vigilance, and pressure resilience.",
    },
}

# 25 Vibrant, situation-based, non-boring questions (5 per trait)
# Reverse items prevent straight-lining and acquiescence bias.
QUESTIONS = {
    "Openness": [
        {
            "id": "O1",
            "text": "I easily fall down 2 AM rabbit holes researching bizarre mysteries, abstract science, or eccentric subcultures.",
            "reverse": False,
        },
        {
            "id": "O2",
            "text": "If I spot an unfamiliar, weird-looking street food dish in a night market, I'm ordering it without hesitation.",
            "reverse": False,
        },
        {
            "id": "O3",
            "text": "I constantly daydream about wild 'what-if' scenarios, alternative realities, or crazy futuristic inventions.",
            "reverse": False,
        },
        {
            "id": "O4",
            "text": "I'd much rather re-watch my safe comfort TV show for the 10th time than gamble my evening on a quirky indie film.",
            "reverse": True,
        },
        {
            "id": "O5",
            "text": "I get genuinely energized by deep philosophical arguments that don't have neat, black-and-white answers.",
            "reverse": False,
        },
    ],
    "Conscientiousness": [
        {
            "id": "C1",
            "text": "My room or desktop looks like a category 5 hurricane hit it, but I insist it's 'organized chaos.'",
            "reverse": True,
        },
        {
            "id": "C2",
            "text": "If I commit to a deadline or promise someone a deliverable, I will move mountains before breaking it.",
            "reverse": False,
        },
        {
            "id": "C3",
            "text": "Crossing off completed tasks on a neatly structured to-do list gives me a distinct surge of dopamine.",
            "reverse": False,
        },
        {
            "id": "C4",
            "text": "I tend to launch ambitious new hobbies or side projects with intense fire, then abandon them at 35% completion.",
            "reverse": True,
        },
        {
            "id": "C5",
            "text": "Before taking any trip or initiating a project, I've already mapped out a backup plan for the backup plan.",
            "reverse": False,
        },
    ],
    "Extraversion": [
        {
            "id": "E1",
            "text": "After a high-energy gathering or packed party, I feel like a fully charged battery rather than drained.",
            "reverse": False,
        },
        {
            "id": "E2",
            "text": "In an awkwardly silent elevator, waiting room, or team call, I'm almost always the one to break the ice.",
            "reverse": False,
        },
        {
            "id": "E3",
            "text": "I think out loud—I discover what I truly believe while speaking, rather than ruminating in quiet solitude.",
            "reverse": False,
        },
        {
            "id": "E4",
            "text": "My absolute dream evening is putting my phone on 'Do Not Disturb' and not interacting with a single human soul.",
            "reverse": True,
        },
        {
            "id": "E5",
            "text": "If karaoke starts or a group suddenly needs a speaker, my hand goes up before my rational brain can stop me.",
            "reverse": False,
        },
    ],
    "Agreeableness": [
        {
            "id": "A1",
            "text": "If someone walks into the room with subtle hidden sadness or tension, I pick up on their vibe in seconds.",
            "reverse": False,
        },
        {
            "id": "A2",
            "text": "I'd rather yield on a petty disagreement than create awkward lingering friction with someone I care about.",
            "reverse": False,
        },
        {
            "id": "A3",
            "text": "I naturally give strangers the benefit of the doubt and assume good intentions until proven otherwise.",
            "reverse": False,
        },
        {
            "id": "A4",
            "text": "I prioritize blunt, unvarnished honesty over etiquette—if the truth hurts someone's feelings, so be it.",
            "reverse": True,
        },
        {
            "id": "A5",
            "text": "I frequently end up being the unofficial therapist and peacekeeper for my circle of friends or coworkers.",
            "reverse": False,
        },
    ],
    "Neuroticism": [
        {
            "id": "N1",
            "text": "When a boss or friend texts 'Hey, do you have a quick minute to talk?', my brain brainstorms 15 catastrophic crises.",
            "reverse": False,
        },
        {
            "id": "N2",
            "text": "I occasionally replay an embarrassing comment I made four years ago while staring at the ceiling at 3 AM.",
            "reverse": False,
        },
        {
            "id": "N3",
            "text": "When sudden unexpected crisis strikes, I instantly switch into cold, collected tactical problem-solving mode.",
            "reverse": True,
        },
        {
            "id": "N4",
            "text": "My internal energy can pivot from 'I am invincible' to 'I am entirely burnt out' in the span of a single afternoon.",
            "reverse": False,
        },
        {
            "id": "N5",
            "text": "Constructive criticism or a tiny perceived snub can linger in my head and ruin my mood for the rest of the day.",
            "reverse": False,
        },
    ],
}


def score_responses(responses):
    """Return trait scores scaled from 0 to 100 using a 1–5 response scale."""
    scores = {}
    for trait, items in QUESTIONS.items():
        values = []
        for item in items:
            val = responses.get(item["id"], 3)
            if item["reverse"]:
                val = 6 - val
            values.append(val)
        mean_score = sum(values) / len(values)
        scores[trait] = round(((mean_score - 1) / 4) * 100, 1)
    return scores


def interpretation(score):
    """Return a non-clinical score band."""
    if score < 36:
        return "Low Range", "Subtle / Grounded"
    elif score <= 65:
        return "Balanced Range", "Flexible / Situation-dependent"
    else:
        return "High Range", "Prominent / Driving"


def trait_description(trait, score):
    """Return dynamic, nuanced interpretation and breakdown."""
    level, _ = interpretation(score)

    descriptions = {
        "Openness": {
            "Low Range": (
                "Pragmatic, grounded, and focused on tangible reality. You value proven methods over theoretical speculation "
                "and prefer dependable routines that work rather than reinventions for novelty's sake."
            ),
            "Balanced Range": (
                "Pragmatically imaginative. You appreciate fresh concepts and creative viewpoints, but keep one foot firmly "
                "planted in reality. You know when to experiment and when to stick with what works."
            ),
            "High Range": (
                "Boundlessly inquisitive, imaginative, and conceptually bold. You thrive on unconventional concepts, aesthetic depth, "
                "and mental exploration. You view routine as an invitation to innovate."
            ),
        },
        "Conscientiousness": {
            "Low Range": (
                "Spontaneous, adaptable, and flexible. You excel in fluid situations that stifle rigid planners. You prefer to follow "
                "creative flow rather than adhere to strict calendars."
            ),
            "Balanced Range": (
                "Strategically organized. You maintain solid follow-through and organizational structure where it matters most, "
                "while preserving enough agility to pivot whenever life throws a curveball."
            ),
            "High Range": (
                "Methodical, ultra-reliable, and intrinsically driven. When you commit to a mission, you bring deliberate planning, "
                "exceptional accountability, and laser focus to see it across the finish line."
            ),
        },
        "Extraversion": {
            "Low Range": (
                "Reflective, independent, and self-contained. You draw your deepest energy from solitary focus or intimate one-on-one "
                "conversations. You listen deeply and speak with measured intention."
            ),
            "Balanced Range": (
                "Ambiverted social chameleon. You comfortably command a room or mingle at lively events, yet you equally cherish "
                "uninterrupted downtime to recharge your internal batteries."
            ),
            "High Range": (
                "Radiant, socially magnetic, and naturally expressive. You are energized by crowds, lively dialogue, and shared adventures. "
                "You bring warmth, spark, and momentum into any group dynamic."
            ),
        },
        "Agreeableness": {
            "Low Range": (
                "Candid, independent, and fiercely analytical. You prioritize truth, rigorous objectivity, and direct feedback over social "
                "niceties. You aren't afraid to challenge consensus to get to facts."
            ),
            "Balanced Range": (
                "Equitable and discerning. You are compassionate and cooperative by default, but you maintain firm boundaries and won't "
                "hesitate to advocate for yourself or speak hard truths when necessary."
            ),
            "High Range": (
                "Deeply empathetic, altruistic, and harmonizing. You instinctively perceive others' emotional needs, foster psychological safety, "
                "and build bridges across differing viewpoints."
            ),
        },
        "Neuroticism": {
            "Low Range": (
                "Emotionally steady, unflappable, and resilient. You maintain remarkable composure in high-stress storms, bouncing back from "
                "setbacks with calm perspective and low baseline anxiety."
            ),
            "Balanced Range": (
                "Attuned and context-responsive. You feel the natural spikes of life's stress and urgency, but you generally self-regulate and "
                "regain your footing before emotional waves derail you."
            ),
            "High Range": (
                "Deeply perceptive, vigilant, and emotionally intense. You experience the emotional nuances of life with high sensitivity. "
                "While stress can feel visceral, this same trait fuels remarkable empathy, risk-anticipation, and artistic depth."
            ),
        },
    }

    return level, descriptions[trait][level]


def get_personality_archetype(scores):
    """Derive an engaging, memorable personality persona archetype based on the trait synergy."""
    o, c, e, a, n = (
        scores["Openness"],
        scores["Conscientiousness"],
        scores["Extraversion"],
        scores["Agreeableness"],
        scores["Neuroticism"],
    )

    # Sort dominant positive traits
    sorted_traits = sorted(
        [("Openness", o), ("Conscientiousness", c), ("Extraversion", e), ("Agreeableness", a)],
        key=lambda x: x[1],
        reverse=True,
    )
    primary_trait, primary_score = sorted_traits[0]
    secondary_trait, secondary_score = sorted_traits[1]

    # Archetype selection matrix
    if primary_trait == "Openness" and secondary_trait == "Conscientiousness":
        return {
            "title": "The Visionary Architect",
            "icon": "🏛️",
            "tagline": "Unbridled imagination backed by surgical execution.",
            "bio": (
                "You combine rare conceptual foresight with the methodical drive to turn abstract dreams into tangible reality. "
                "While others get lost in contemplation or stuck in mechanical routine, you bridge the gap between poetry and engineering."
            ),
            "superpowers": [
                "Translating complex, innovative visions into actionable blueprints",
                "Relentless intellectual curiosity coupled with disciplined follow-through",
                "High tolerance for ambiguity without sacrificing organizational rigor",
            ],
            "growth_areas": [
                "Avoid falling into perfectionism paralysis when an 85% solution is already brilliant.",
                "Leave room for spontaneous detours; sometimes messy iterations beat rigid perfection.",
            ],
            "ideal_environment": "Pioneering R&D hubs, product architecture, creative direction, strategic leadership.",
        }

    elif primary_trait == "Openness" and secondary_trait == "Extraversion":
        return {
            "title": "The Trailblazing Catalyst",
            "icon": "🚀",
            "tagline": "Infectious charisma championing cutting-edge ideas.",
            "bio": (
                "You are an idea powerhouse who breathes life into bold concepts through vibrant storytelling and social magnetism. "
                "You rally people around unorthodox visions and inspire others to step outside comfortable boundaries."
            ),
            "superpowers": [
                "Pitching transformative, unconventional ideas with infectious passion",
                "Cross-pollinating diverse groups, concepts, and cultural spheres",
                "Effortlessly energizing teams through humor and spontaneous creativity",
            ],
            "growth_areas": [
                "Partner with meticulous planners to ensure your grand fireworks culminate in solid long-term execution.",
                "Protect regular quiet focus blocks so ideas have space to crystallize before sharing.",
            ],
            "ideal_environment": "Innovation labs, public evangelism, high-growth entrepreneurship, media & creative direction.",
        }

    elif primary_trait == "Conscientiousness" and secondary_trait == "Extraversion":
        return {
            "title": "The Executive Dynamo",
            "icon": "⚡",
            "tagline": "Decisive momentum, high accountability, and unstoppable drive.",
            "bio": (
                "A force of nature in any team or enterprise. You don't just set audacious goals—you mobilize people, establish clear structures, "
                "and execute with unwavering momentum. Your presence instills clarity and velocity."
            ),
            "superpowers": [
                "Exceptional operational clarity and decisive leadership under tight timelines",
                "Holding yourself and teams to inspiring standards of excellence",
                "Channeling group energy toward measurable, meaningful milestones",
            ],
            "growth_areas": [
                "Remember that not everyone works at 120 mph; cultivate patience for slower, deliberate processors.",
                "Celebrate milestone wins before immediately leaping to the next mountain peak.",
            ],
            "ideal_environment": "Operations leadership, competitive entrepreneurship, project direction, venture strategy.",
        }

    elif primary_trait == "Agreeableness" and secondary_trait == "Extraversion":
        return {
            "title": "The Radiant Harmonizer",
            "icon": "🌟",
            "tagline": "Magnetic empathy uniting communities and lifting spirits.",
            "bio": (
                "You possess a natural warmth that disarms cynics and dissolves tension. People feel seen, heard, and energized in your presence. "
                "You build social bridges where others see walls, serving as the cultural heart of your circles."
            ),
            "superpowers": [
                "Intuitive social intelligence and instant rapport building",
                "Transforming stressful environments into welcoming, collaborative safe havens",
                "Mediating disagreements with grace, humor, and sincere goodwill",
            ],
            "growth_areas": [
                "Guard your personal boundaries fiercely; not every crisis requires you to be the emotional shock absorber.",
                "Practice delivering direct, uncomfortable feedback without softening it to the point of ambiguity.",
            ],
            "ideal_environment": "People operations, team leadership, community building, coaching, client advocacy.",
        }

    elif primary_trait == "Conscientiousness" and secondary_trait == "Agreeableness":
        return {
            "title": "The Guardian Anchor",
            "icon": "🛡️",
            "tagline": "Unshakable integrity, quiet dependability, and heartfelt loyalty.",
            "bio": (
                "You are the bedrock that organizations and families rely on. Methodical, considerate, and deeply principled, "
                "you protect standards and care for people with equal devotion. Your word is your bond."
            ),
            "superpowers": [
                "Flawless reliability and exceptional ethical follow-through",
                "Creating orderly, safe, and supportive environments where others flourish",
                "Quiet diligence that anticipates problems before anyone else notices them",
            ],
            "growth_areas": [
                "Be comfortable saying 'no' to non-essential requests that drain your personal reserves.",
                "Embrace constructive conflict as a healthy tool for team innovation rather than something to avoid.",
            ],
            "ideal_environment": "Healthcare, institutional management, operational governance, counseling, trusted advising.",
        }

    elif primary_trait == "Openness" and secondary_trait == "Agreeableness":
        return {
            "title": "The Empathetic Philosopher",
            "icon": "🌌",
            "tagline": "Compassionate insight exploring the depths of the human experience.",
            "bio": (
                "You combine an expansive curiosity about life with a tender heart for living beings. You look beyond surface appearances, "
                "seeking philosophical meaning, aesthetic resonance, and deep human connection."
            ),
            "superpowers": [
                "Profound emotional nuance and holistic intuitive thinking",
                "Ability to understand radically divergent viewpoints without judgment",
                "Artistic and conceptual synthesis of human emotions and stories",
            ],
            "growth_areas": [
                "Ground your rich internal universe into concrete, daily bite-sized actions.",
                "Shield yourself from absorbing collective negative news cycles and world anxieties.",
            ],
            "ideal_environment": "Creative writing, psychotherapy, design research, education, non-profit visioning.",
        }

    elif primary_trait == "Conscientiousness" and n < 40:
        return {
            "title": "The Zen Strategist",
            "icon": "♟️",
            "tagline": "Unflinching composure, sharp focus, and long-range tactical mastery.",
            "bio": (
                "When panic grips the room, your pulse stays steady. You assess chaotic landscapes with cool detachment, calculate "
                "optimal moves, and execute methodically. Stress bounces off your armor."
            ),
            "superpowers": [
                "Superhuman composure under extreme pressure and high stakes",
                "Objective, noise-free problem evaluation without emotional distortion",
                "Systemic thinking that guarantees sustainable, compounding results",
            ],
            "growth_areas": [
                "Communicate your internal reasoning openly; teammates may misread your calm as indifference.",
                "Allow room for intuition and gut feel alongside strict spreadsheet logic.",
            ],
            "ideal_environment": "Crisis response, portfolio management, engineering leadership, systems architecture.",
        }

    elif primary_trait == "Extraversion" and o > 60:
        return {
            "title": "The Renaissance Spark",
            "icon": "✨",
            "tagline": "Dynamic energy, multifaceted interests, and contagious enthusiasm.",
            "bio": (
                "A whirlwind of curiosity, connections, and experiments. You despise boring routine and thrive at the intersection "
                "of people, arts, ideas, and high-energy exploration. There's never a dull moment around you."
            ),
            "superpowers": [
                "Electrifying enthusiasm that shakes people out of complacency",
                "Mastery at initiating new ventures, conversations, and creative jams",
                "Fearless social confidence in novel environments",
            ],
            "growth_areas": [
                "Practice finishing the last 15% of your endeavors with the same gusto as the first 15%.",
                "Carve out moments of stillness to avoid overstimulation burnout.",
            ],
            "ideal_environment": "Creative agencies, event production, startup founding, dynamic public speaking.",
        }

    else:
        # Fallback to dominant primary trait archetype
        single_archetypes = {
            "Openness": {
                "title": "The Free-Spirited Explorer",
                "icon": "🧭",
                "tagline": "Pioneering curiosity unconstrained by traditional convention.",
                "bio": "You march to your own drumbeat, driven by an endless appetite for discovery, originality, and intellectual wonder.",
                "superpowers": ["Original conceptual thinking", "Unafraid of novelty", "Rich imaginative depth"],
                "growth_areas": ["Anchor thoughts in concrete deliverables", "Cultivate everyday consistency"],
                "ideal_environment": "Creative studios, research think tanks, speculative design.",
            },
            "Conscientiousness": {
                "title": "The Master Craftsman",
                "icon": "⚙️",
                "tagline": "Impeccable discipline, methodical mastery, and gold-standard execution.",
                "bio": "You turn ambition into art through rigorous preparation, unwavering standards, and steadfast accountability.",
                "superpowers": ["Flawless focus", "Systemic dependability", "High resistance to distraction"],
                "growth_areas": ["Embrace serendipity and imperfect iterations", "Avoid hyper-critical self-assessment"],
                "ideal_environment": "Specialized engineering, project mastery, strategic analytics.",
            },
            "Extraversion": {
                "title": "The Social Luminary",
                "icon": "🔥",
                "tagline": "Magnetic presence, boundless stamina, and heart of the collective.",
                "bio": "You bring life, excitement, and forward motion to every room you enter, thriving on shared experiences and connection.",
                "superpowers": ["Charismatic rapport", "Vocal advocacy", "Spontaneous group energizer"],
                "growth_areas": ["Practice active listening without rushing to respond", "Cherish solo reflection time"],
                "ideal_environment": "Public relations, venture growth, dynamic sales, live production.",
            },
            "Agreeableness": {
                "title": "The Compassionate Guardian",
                "icon": "🕊️",
                "tagline": "Gentle strength, empathetic listening, and relational glue.",
                "bio": "You prioritize people over ego, bringing empathy, equity, and peace to every human interaction you nurture.",
                "superpowers": ["Deep emotional resonance", "Selfless support", "Natural trust building"],
                "growth_areas": ["Assert your boundaries unapologetically", "Don't sacrifice your needs for consensus"],
                "ideal_environment": "Humanitarian missions, talent coaching, healthcare, mediation.",
            },
            "Neuroticism": {
                "title": "The Vigilant Intuitive",
                "icon": "⚡",
                "tagline": "Hypersensitive radar, emotional depth, and acute foresight.",
                "bio": "Your radar is tuned to subtle frequencies others miss. While stress hits deeply, your vigilance shields groups from hidden risks.",
                "superpowers": ["Acute risk anticipation", "Profound empathy for human suffering", "Deep self-awareness"],
                "growth_areas": ["Build somatic de-stress rituals to discharge tension", "Challenge catastrophizing narratives"],
                "ideal_environment": "Quality assurance, deep artistic expression, risk auditing, safety management.",
            },
        }
        return single_archetypes.get(primary_trait, single_archetypes["Openness"])
