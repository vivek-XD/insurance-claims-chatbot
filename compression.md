import nltk
from nltk.chat.util import Chat, reflections

# Insurance claim ke liye patterns aur responses
pairs = [
    [
        r"hi|hello|hey",
        ["Namaste! Insurance claim mein madad chahiye? New claim, status ya process bataun?", "Hello! Kya aap claim file karna chahte ho?"]
    ],
    [
        r"new claim|claim file|claim start",
        ["Theek hai. Policy number bataiye.", "New claim shuru karte hain. Aapka policy number kya hai?"]
    ],
    [
        r"status check|claim status|track claim",
        ["Claim ID daaliye status check karne ke liye.", "Aapka claim ID share kijiye, main status bataunga."]
    ],
    [
        r"documents|kya documents|required papers",
        ["Claim ke liye ye documents lagenge: 1. Policy copy, 2. FIR (agar accident), 3. Medical bills, 4. Photos. Upload kaise karna hai bataun?", "Zaruri documents: ID proof, incident details, bills aur photos."]
    ],
    [
        r"process|claim process|steps",
        ["Claim process: 1. Details submit, 2. Documents upload, 3. Verification, 4. Approval (7-15 days). Aur kuch?", "Pehle online form bharo, documents attach karo, phir track karo."]
    ],
    [
        r"policy number (.*)",
        ["Policy number noted: %1. Ab incident date bataiye.", "Thanks, policy %1 valid lag raha. Agla step: kab hua accident?"]
    ],
    [
        r"claim id (.*)",
        ["Claim ID %1 ka status: Under review. 2 din mein update milega.", "ID %1 approved hai, payout processing mein."]
    ],
    [
        r"bye|exit|quit",
        ["Dhanyawad! Claim safe rahe. Helpdesk pe call karo agar zarurat ho.", "Bye! Safe rahiye."]
    ],
    [
        r"(.*)",
        ["Sorry, ye samajh nahi aaya. 'New claim' ya 'status' bolo.", "Thoda clear bataiye, claim ke bare mein poochh rahe ho?"]
    ]
]
chatbot = Chat(pairs, reflections)
print("Insurance Claim Bot: Hi! Type 'quit' to exit.")
chatbot.converse()
