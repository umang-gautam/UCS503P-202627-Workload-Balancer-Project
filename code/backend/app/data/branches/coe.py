"""
Thapar Institute of Engineering and Technology (TIET) Patiala
Course Scheme and Syllabus for B.E. (Computer Engineering - COE) 2025-2026.

Extracted directly from the official academic council course scheme document.
"""

COE_PROGRAM_INFO = {
    "branch_code": "COE",
    "branch_name": "Computer Engineering",
    "degree": "B.E.",
    "institution": "Thapar Institute of Engineering and Technology, Patiala",
    "revision": "March 2026",
}

# Real COE students from the project team
COE_STUDENTS = [
    {"name": "Umang Gautam", "email": "ugautam_be24@thapar.edu", "roll_no": "1024030805", "semester": 5},
    {"name": "Vriti Mahajan", "email": "vmahajan1_be24@thapar.edu", "roll_no": "1024030801", "semester": 5},
    {"name": "Khushi", "email": "kkhushi1_be24@thapar.edu", "roll_no": "1024030809", "semester": 5},
    {"name": "Shaurya Garg", "email": "sgarg6_be24@thapar.edu", "roll_no": "1024030800", "semester": 5},
]

COE_COURSES = [
    # ── SEMESTER I ─────────────────────────────────────────────
    {
        "code": "UCB009",
        "name": "Chemistry",
        "semester": 1,
        "category": "BSC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Atomic and Molecular Spectroscopy",
                "assignment": "Spectrophotometry & Beer-Lambert Law Lab",
                "due_days": 10,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [88]},
            },
            {
                "name": "Electrochemistry & Modern Batteries",
                "assignment": "Conductometric Titration & Battery Cells Report",
                "due_days": 18,
                "scores": {"kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [79]},
            },
            {
                "name": "Water Treatment & Analysis",
                "assignment": "Hardness & Reverse Osmosis Analysis",
                "due_days": 24,
                "scores": {"ugautam_be24@thapar.edu": [85], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Fuels & Fuel Cells",
                "assignment": "Calorific Value & Fuel Storage Exercise",
                "due_days": 30,
                "scores": {"vmahajan1_be24@thapar.edu": [90]},
            },
        ],
    },
    {
        "code": "UES103",
        "name": "Programming for Problem Solving",
        "semester": 1,
        "category": "ESC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Computer Fundamentals & Algorithms",
                "assignment": "Flowchart and Pseudocode Formulation",
                "due_days": 4,
                "scores": {"ugautam_be24@thapar.edu": [95], "vmahajan1_be24@thapar.edu": [92]},
            },
            {
                "name": "Control Structures & Iterative Statements",
                "assignment": "Scientific Calculator Implementation in C",
                "due_days": 11,
                "scores": {"kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Functions & Recursion",
                "assignment": "Tower of Hanoi & Stack Simulation",
                "due_days": 17,
                "scores": {"ugautam_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Pointers & Dynamic Memory Allocation",
                "assignment": "Malloc/Free and Pointer Arithmetic Lab",
                "due_days": 25,
                "scores": {"vmahajan1_be24@thapar.edu": [94], "kkhushi1_be24@thapar.edu": [82]},
            },
        ],
    },
    {
        "code": "UES013",
        "name": "Electrical & Electronics Engineering",
        "semester": 1,
        "category": "ESC",
        "credits": 4.5,
        "topics": [
            {
                "name": "DC Circuits & Network Theorems",
                "assignment": "Thevenin & Norton Theorem Circuit Lab",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [78], "vmahajan1_be24@thapar.edu": [84]},
            },
            {
                "name": "AC Circuits & Phasor Representation",
                "assignment": "RLC Resonance & 3-Phase Power Measurement",
                "due_days": 15,
                "scores": {"kkhushi1_be24@thapar.edu": [72], "sgarg6_be24@thapar.edu": [76]},
            },
            {
                "name": "Digital Logic Design & Karnaugh Maps",
                "assignment": "Logic Gate Minimization & Decoder Design",
                "due_days": 22,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [91]},
            },
            {
                "name": "Electronic Devices & Op-Amp Circuits",
                "assignment": "BJT Switch & Inverting Amplifier Lab",
                "due_days": 28,
                "scores": {"kkhushi1_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [82]},
            },
        ],
    },
    {
        "code": "UEN008",
        "name": "Energy and Environment",
        "semester": 1,
        "category": "OTH",
        "credits": 2.0,
        "topics": [
            {
                "name": "Environmental Pollution & Control",
                "assignment": "Air & Water Quality Index Assessment",
                "due_days": 12,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [86]},
            },
            {
                "name": "Renewable Energy Resources",
                "assignment": "Solar & Biomass System Feasibility Study",
                "due_days": 26,
                "scores": {"kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },
    {
        "code": "UMA022",
        "name": "Calculus for Engineers",
        "semester": 1,
        "category": "BSC",
        "credits": 3.5,
        "topics": [
            {
                "name": "Infinite Series & Convergence Tests",
                "assignment": "Ratio & Integral Test Problem Set",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [89]},
            },
            {
                "name": "Partial Differentiation & Maxima/Minima",
                "assignment": "Directional Derivatives & Optimization",
                "due_days": 14,
                "scores": {"kkhushi1_be24@thapar.edu": [75], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Multiple Integrals & Complex Analysis",
                "assignment": "Double Integrals & Cauchy-Riemann Verification",
                "due_days": 23,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [92]},
            },
        ],
    },

    # ── SEMESTER II ────────────────────────────────────────────
    {
        "code": "UPH013",
        "name": "Physics",
        "semester": 2,
        "category": "BSC",
        "credits": 4.5,
        "topics": [
            {
                "name": "Oscillations, Waves & Acoustics",
                "assignment": "Damped Harmonic Motion & Reverberation Time",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [78], "vmahajan1_be24@thapar.edu": [85]},
            },
            {
                "name": "Electromagnetic Waves & Maxwell Equations",
                "assignment": "Wave Propagation in Conducting Media",
                "due_days": 16,
                "scores": {"kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Wave Optics & Lasers",
                "assignment": "Newton Rings & Diffraction Grating Lab",
                "due_days": 24,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [90]},
            },
            {
                "name": "Quantum Mechanics & Schrodinger Equation",
                "assignment": "Particle in 1D Box & Tunneling Analysis",
                "due_days": 29,
                "scores": {"kkhushi1_be24@thapar.edu": [76], "sgarg6_be24@thapar.edu": [82]},
            },
        ],
    },
    {
        "code": "UES101",
        "name": "Engineering Drawing",
        "semester": 2,
        "category": "ESC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Orthographic & Isometric Projections",
                "assignment": "Missing Views and 3D Solid Projections",
                "due_days": 9,
                "scores": {"ugautam_be24@thapar.edu": [76], "vmahajan1_be24@thapar.edu": [80]},
            },
            {
                "name": "2D Drafting & 3D Modeling (CAD)",
                "assignment": "AutoCAD/SolidWorks Machine Part Modeling",
                "due_days": 21,
                "scores": {"kkhushi1_be24@thapar.edu": [85], "sgarg6_be24@thapar.edu": [88]},
            },
        ],
    },
    {
        "code": "UHU003",
        "name": "Professional Communication",
        "semester": 2,
        "category": "HSS",
        "credits": 3.0,
        "topics": [
            {
                "name": "Interpersonal & Oral Communication",
                "assignment": "Simulated Group Discussion & Presentation",
                "due_days": 13,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [92]},
            },
            {
                "name": "Technical Writing & Business Reports",
                "assignment": "Professional Resume and Formal Technical Report",
                "due_days": 22,
                "scores": {"kkhushi1_be24@thapar.edu": [94], "sgarg6_be24@thapar.edu": [86]},
            },
        ],
    },
    {
        "code": "UES102",
        "name": "Manufacturing Processes",
        "semester": 2,
        "category": "ESC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Machining, Casting & Joining Processes",
                "assignment": "CNC Turning & Arc Welding Fabrication Lab",
                "due_days": 14,
                "scores": {"ugautam_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Smart Manufacturing & Metrology",
                "assignment": "IoT-Enabled Quality Inspection Case Study",
                "due_days": 25,
                "scores": {"vmahajan1_be24@thapar.edu": [86], "kkhushi1_be24@thapar.edu": [82]},
            },
        ],
    },
    {
        "code": "UMA023",
        "name": "Differential Equations and Linear Algebra",
        "semester": 2,
        "category": "BSC",
        "credits": 3.5,
        "topics": [
            {
                "name": "Higher Order Differential Equations",
                "assignment": "Cauchy-Euler & Variation of Parameters Problem Set",
                "due_days": 5,
                "scores": {"ugautam_be24@thapar.edu": [74], "vmahajan1_be24@thapar.edu": [88]},
            },
            {
                "name": "Laplace Transforms & Fourier Series",
                "assignment": "Initial Value & Heat Equation Solutions",
                "due_days": 15,
                "scores": {"kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Vector Spaces & Matrix Diagonalization",
                "assignment": "Gram-Schmidt & Eigenvector Computation Lab",
                "due_days": 23,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [94]},
            },
        ],
    },

    # ── SEMESTER III ───────────────────────────────────────────
    {
        "code": "UCS303",
        "name": "Operating System",
        "semester": 3,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Introduction and System Structures",
                "assignment": "System Calls & Linux Shell Architecture Exploration",
                "due_days": 4,
                "scores": {"ugautam_be24@thapar.edu": [72], "vmahajan1_be24@thapar.edu": [68], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Process Management & CPU Scheduling",
                "assignment": "Multi-Level Feedback Queue Scheduler Simulation",
                "due_days": 9,
                "scores": {"ugautam_be24@thapar.edu": [65], "vmahajan1_be24@thapar.edu": [75], "kkhushi1_be24@thapar.edu": [94], "sgarg6_be24@thapar.edu": [88]},
            },
            {
                "name": "Deadlock Handling & Synchronization",
                "assignment": "Banker's Algorithm & Dining Philosophers with Semaphores",
                "due_days": 13,
                "scores": {"ugautam_be24@thapar.edu": [44, 50], "vmahajan1_be24@thapar.edu": [64], "kkhushi1_be24@thapar.edu": [85], "sgarg6_be24@thapar.edu": [78]},
            },
            {
                "name": "Memory Management & Demand Paging",
                "assignment": "Page Replacement Algorithms (LRU vs Optimal)",
                "due_days": 20,
                "scores": {"ugautam_be24@thapar.edu": [68], "vmahajan1_be24@thapar.edu": [74], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "File Systems & Disk Management",
                "assignment": "File Allocation & RAID Storage Architecture Benchmark",
                "due_days": 27,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [92], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },
    {
        "code": "UTA018",
        "name": "Object Oriented Programming",
        "semester": 3,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Classes, Encapsulation & Constructors",
                "assignment": "Smart City Energy Grid Class Hierarchy in C++",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Inheritance & Polymorphism",
                "assignment": "Virtual Functions & Transportation System Simulation",
                "due_days": 14,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [95], "kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Templates, STL & Exception Handling",
                "assignment": "Generic Containers & Custom Exception Handler",
                "due_days": 23,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [96], "kkhushi1_be24@thapar.edu": [86], "sgarg6_be24@thapar.edu": [90]},
            },
        ],
    },
    {
        "code": "UCS301",
        "name": "Data Structures",
        "semester": 3,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Algorithm Analysis & Linear Structures",
                "assignment": "Linked List, Stack & Queue ADT Performance Comparison",
                "due_days": 4,
                "scores": {"ugautam_be24@thapar.edu": [75], "vmahajan1_be24@thapar.edu": [94], "kkhushi1_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Searching, Sorting & Hash Tables",
                "assignment": "Collision Resolution & Quick/Merge Sort Benchmarks",
                "due_days": 10,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [96], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Trees, AVL Trees & Heaps",
                "assignment": "Self-Balancing AVL & Priority Queue Implementation",
                "due_days": 18,
                "scores": {"ugautam_be24@thapar.edu": [62, 68], "vmahajan1_be24@thapar.edu": [92, 95], "kkhushi1_be24@thapar.edu": [54], "sgarg6_be24@thapar.edu": [76]},
            },
            {
                "name": "Graphs & Shortest Path Algorithms",
                "assignment": "Dijkstra, Prim-Kruskal & Disjoint Sets Lab",
                "due_days": 26,
                "scores": {"ugautam_be24@thapar.edu": [42, 48], "vmahajan1_be24@thapar.edu": [88, 90], "kkhushi1_be24@thapar.edu": [70], "sgarg6_be24@thapar.edu": [64]},
            },
        ],
    },
    {
        "code": "UCS405",
        "name": "Discrete Mathematical Structures",
        "semester": 3,
        "category": "PCC",
        "credits": 3.5,
        "topics": [
            {
                "name": "Sets, Relations, Functions & Posets",
                "assignment": "Equivalence Relations & Hasse Diagram Verification",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [85], "kkhushi1_be24@thapar.edu": [75], "sgarg6_be24@thapar.edu": [78]},
            },
            {
                "name": "Graph Theory & Combinatorics",
                "assignment": "Eulerian Paths, Planar Graphs & Graph Coloring",
                "due_days": 15,
                "scores": {"ugautam_be24@thapar.edu": [72], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [70], "sgarg6_be24@thapar.edu": [75]},
            },
            {
                "name": "Propositional Logic & Recurrence Relations",
                "assignment": "Proof Techniques & Divide-and-Conquer Recurrences",
                "due_days": 25,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [84]},
            },
        ],
    },
    {
        "code": "UTA016",
        "name": "Engineering Design Project I",
        "semester": 3,
        "category": "ESC",
        "credits": 3.0,
        "topics": [
            {
                "name": "CDIO Methodology & Mangonel Modeling",
                "assignment": "Catapult Trajectory Simulator with Drag",
                "due_days": 12,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [85], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Sensor Interfacing & Arduino Control",
                "assignment": "Angular Velocity Measurement & Throwing Arm Redesign",
                "due_days": 25,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [89], "kkhushi1_be24@thapar.edu": [94], "sgarg6_be24@thapar.edu": [91]},
            },
        ],
    },
    {
        "code": "UMA021",
        "name": "Numerical Linear Algebra",
        "semester": 3,
        "category": "BSC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Roots of Non-Linear Equations",
                "assignment": "Newton-Raphson & Multi-Equation Solver in MATLAB",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Matrix Factorization & Eigenvalue Methods",
                "assignment": "QR Algorithm & SVD Computation Experiment",
                "due_days": 21,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [88]},
            },
        ],
    },
    {
        "code": "UCS320",
        "name": "Introduction to Sustainable Green Computing",
        "semester": 3,
        "category": "PCC",
        "credits": 1.0,
        "topics": [
            {
                "name": "Principles of Green Computing & Energy-Aware Design",
                "assignment": "Data Center Energy Profiling & Carbon Footprint Audit",
                "due_days": 16,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [89]},
            },
        ],
    },

    # ── SEMESTER IV ────────────────────────────────────────────
    {
        "code": "UCS415",
        "name": "Design and Analysis of Algorithms",
        "semester": 4,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Asymptotic Analysis & Divide-and-Conquer",
                "assignment": "Strassen Matrix Multiplication & Master Theorem",
                "due_days": 5,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [78]},
            },
            {
                "name": "Greedy Algorithms & Dynamic Programming",
                "assignment": "0/1 Knapsack & Longest Common Subsequence Lab",
                "due_days": 12,
                "scores": {"ugautam_be24@thapar.edu": [70], "vmahajan1_be24@thapar.edu": [86], "kkhushi1_be24@thapar.edu": [62], "sgarg6_be24@thapar.edu": [45, 50]},
            },
            {
                "name": "Backtracking & Branch-and-Bound",
                "assignment": "N-Queens & Traveling Salesperson Implementation",
                "due_days": 19,
                "scores": {"ugautam_be24@thapar.edu": [78], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [68], "sgarg6_be24@thapar.edu": [60]},
            },
            {
                "name": "Graph Algorithms & String Matching",
                "assignment": "Ford-Fulkerson Max Flow & KMP Algorithm",
                "due_days": 27,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [76], "sgarg6_be24@thapar.edu": [72]},
            },
        ],
    },
    {
        "code": "UCS310",
        "name": "Database Management Systems",
        "semester": 4,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Relational Model & Conceptual ER Design",
                "assignment": "Hospital Management ER Diagram & Table Schema",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [84], "kkhushi1_be24@thapar.edu": [76], "sgarg6_be24@thapar.edu": [88]},
            },
            {
                "name": "Functional Dependencies & Normalization (1NF-5NF)",
                "assignment": "3NF & BCNF Decomposition Exercise",
                "due_days": 14,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [76], "kkhushi1_be24@thapar.edu": [70], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Transactions, ACID & Concurrency Control",
                "assignment": "Two-Phase Locking & Serializability Verification",
                "due_days": 22,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [78], "kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [90]},
            },
            {
                "name": "Advanced SQL & PL/SQL Stored Procedures",
                "assignment": "Complex Joins, Cursors and Database Triggers Lab",
                "due_days": 28,
                "scores": {"ugautam_be24@thapar.edu": [95], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [92]},
            },
        ],
    },
    {
        "code": "UCS414",
        "name": "Computer Networks",
        "semester": 4,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Network Architecture & Local Area Networks",
                "assignment": "GNS3 Topology Setup & Packet Capture Analysis",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [52, 58], "kkhushi1_be24@thapar.edu": [92], "sgarg6_be24@thapar.edu": [75]},
            },
            {
                "name": "Reliable Delivery & Flow Control",
                "assignment": "Sliding Window Protocol Simulator",
                "due_days": 13,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [65], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Routing & Forwarding (IP, OSPF, BGP)",
                "assignment": "CIDR Subnetting & Dijkstra Shortest Path Routing",
                "due_days": 20,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [70], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Transport & Application Protocols (TCP/UDP, DNS)",
                "assignment": "Socket Programming & Multi-Threaded HTTP Server",
                "due_days": 28,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [80], "kkhushi1_be24@thapar.edu": [95], "sgarg6_be24@thapar.edu": [86]},
            },
        ],
    },
    {
        "code": "UCS321",
        "name": "AI for Engineers",
        "semester": 4,
        "category": "PCC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Introduction to AI & Data Preprocessing",
                "assignment": "Sensor Data Cleaning & Feature Scaling with scikit-learn",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [86], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [85]},
            },
            {
                "name": "Supervised & Unsupervised Learning",
                "assignment": "Equipment Failure Prediction using Random Forest & K-Means",
                "due_days": 16,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [85], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Neural Networks & Time-Series Forecasting",
                "assignment": "Structural Crack Detection with CNNs & ARIMA",
                "due_days": 24,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [78]},
            },
        ],
    },
    {
        "code": "UMA401",
        "name": "Probability and Statistics",
        "semester": 4,
        "category": "BSC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Probability Theory & Bayes' Theorem",
                "assignment": "Conditional Probability & Medical Testing Problem Set",
                "due_days": 5,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [91], "kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Distributions & Central Limit Theorem",
                "assignment": "Normal, Binomial & Poisson Distribution Analysis in R",
                "due_days": 15,
                "scores": {"ugautam_be24@thapar.edu": [78], "vmahajan1_be24@thapar.edu": [89], "kkhushi1_be24@thapar.edu": [70], "sgarg6_be24@thapar.edu": [76]},
            },
            {
                "name": "Statistical Estimation & Hypothesis Testing",
                "assignment": "t-Test & Chi-Square Goodness of Fit Implementation",
                "due_days": 25,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [94], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },

    # ── SEMESTER V (Current Core Semester) ─────────────────────
    {
        "code": "UCS503",
        "name": "Software Engineering",
        "semester": 5,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Software Engineering & Evolutionary Process Models",
                "assignment": "Process Models Comparison & Green IT Analysis",
                "due_days": 3,
                "scores": {"ugautam_be24@thapar.edu": [88, 92], "vmahajan1_be24@thapar.edu": [78, 82], "kkhushi1_be24@thapar.edu": [65, 70], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Requirements Engineering & SRS Documentation",
                "assignment": "SRS Document & Use Case Specifications",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [80], "kkhushi1_be24@thapar.edu": [72], "sgarg6_be24@thapar.edu": [84]},
            },
            {
                "name": "Software Design & Architecture (MVC, Microservices)",
                "assignment": "UML Component, Sequence & Class Diagrams",
                "due_days": 12,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [72, 75], "kkhushi1_be24@thapar.edu": [48, 52], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Software Verification, Validation & Testing Strategies",
                "assignment": "Unit & Integration Test Suites with Coverage",
                "due_days": 20,
                "scores": {"ugautam_be24@thapar.edu": [75], "vmahajan1_be24@thapar.edu": [55, 60], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [58, 62]},
            },
            {
                "name": "Agile Methodologies (Scrum, XP, TDD & User Stories)",
                "assignment": "Sprint Backlog Planning & Energy-Aware UX Design",
                "due_days": 28,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [85], "kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [88]},
            },
        ],
    },
    {
        "code": "UML501",
        "name": "Machine Learning",
        "semester": 5,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Data Preprocessing & Feature Scaling",
                "assignment": "Data Cleaning & Normalization Pipeline in Python",
                "due_days": 5,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [84], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Regression Models & Regularization",
                "assignment": "Multiple Linear & Ridge/Lasso Polynomial Regression",
                "due_days": 11,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [75]},
            },
            {
                "name": "Classification Algorithms (Decision Trees, SVM, KNN)",
                "assignment": "Classifier Evaluation with ROC/AUC and F1-Score",
                "due_days": 18,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [94], "kkhushi1_be24@thapar.edu": [70], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Clustering, Association Rules & Neural Networks",
                "assignment": "K-Means Poverty Mapping & Backpropagation MLP",
                "due_days": 26,
                "scores": {"ugautam_be24@thapar.edu": [76], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [65], "sgarg6_be24@thapar.edu": [72]},
            },
        ],
    },
    {
        "code": "UCS553",
        "name": "Enterprise Web Application",
        "semester": 5,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Java Fundamentals & Object-Oriented Architecture",
                "assignment": "Core Java Class Model with Packages and Access Rules",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [90]},
            },
            {
                "name": "Collections Framework & Generics",
                "assignment": "Student Records Manager with HashMaps and Comparators",
                "due_days": 13,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [85], "kkhushi1_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [88]},
            },
            {
                "name": "JDBC, DAO Design Pattern & Transaction Management",
                "assignment": "Database-Driven Inventory System with PreparedStatement",
                "due_days": 21,
                "scores": {"ugautam_be24@thapar.edu": [95], "vmahajan1_be24@thapar.edu": [80], "kkhushi1_be24@thapar.edu": [75], "sgarg6_be24@thapar.edu": [92]},
            },
            {
                "name": "JavaFX GUI & Event-Driven Architecture",
                "assignment": "Interactive Desktop Dashboard with Event Handlers",
                "due_days": 27,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [84], "kkhushi1_be24@thapar.edu": [86], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },
    {
        "code": "UCS615",
        "name": "Image Processing",
        "semester": 5,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Digital Image Fundamentals & Spatial Filtering",
                "assignment": "Histogram Equalization & Spatial Convolution Filters",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [86], "kkhushi1_be24@thapar.edu": [80], "sgarg6_be24@thapar.edu": [78]},
            },
            {
                "name": "Feature Extraction (Canny, SIFT, LBP)",
                "assignment": "Harris Corner & Hough Transform Detection",
                "due_days": 15,
                "scores": {"ugautam_be24@thapar.edu": [78], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Image Segmentation & Morphological Processing",
                "assignment": "Graph-Cut and Region Growing Segmentation",
                "due_days": 22,
                "scores": {"ugautam_be24@thapar.edu": [75], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [72], "sgarg6_be24@thapar.edu": [76]},
            },
            {
                "name": "Deep Learning for Vision (AlexNet, ResNet)",
                "assignment": "CNN-Based Image Classifier in PyTorch",
                "due_days": 29,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },
    {
        "code": "UCS510",
        "name": "Computer Architecture and Organization",
        "semester": 5,
        "category": "PCC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Register Transfer & Micro-Operations (ALU Design)",
                "assignment": "ALU and Shift Micro-Operations Simulation",
                "due_days": 5,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [78], "kkhushi1_be24@thapar.edu": [86], "sgarg6_be24@thapar.edu": [88]},
            },
            {
                "name": "CPU Design, Instruction Formats & Addressing Modes",
                "assignment": "RISC vs CISC Instruction Set Analysis",
                "due_days": 13,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [80], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Instruction Pipelining & Hazard Resolution",
                "assignment": "Pipeline Hazard and Stall Latency Benchmark",
                "due_days": 20,
                "scores": {"ugautam_be24@thapar.edu": [76], "vmahajan1_be24@thapar.edu": [74], "kkhushi1_be24@thapar.edu": [84], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Memory Hierarchy & Cache Mapping Techniques",
                "assignment": "Direct vs Set-Associative Cache Hit Rate Analyzer",
                "due_days": 26,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [82], "kkhushi1_be24@thapar.edu": [92], "sgarg6_be24@thapar.edu": [85]},
            },
        ],
    },
    {
        "code": "UCS421",
        "name": "Ethics and Risk Mitigation in AI",
        "semester": 5,
        "category": "ESC",
        "credits": 3.0,
        "topics": [
            {
                "name": "AI Ethics Principles & Algorithmic Bias",
                "assignment": "Calibration Bias & Fairness Audit on Training Data",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [94], "sgarg6_be24@thapar.edu": [86]},
            },
            {
                "name": "Data Privacy, DPDP Act & GDPR Governance",
                "assignment": "IoT Sensor Compliance & Consent Architecture",
                "due_days": 17,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [85], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Explainable AI (XAI) with SHAP and LIME",
                "assignment": "Interpretable Machine Learning for High-Stakes Decisions",
                "due_days": 25,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [92], "sgarg6_be24@thapar.edu": [89]},
            },
        ],
    },

    # ── SEMESTER VI ────────────────────────────────────────────
    {
        "code": "UCS701",
        "name": "Theory of Computation",
        "semester": 6,
        "category": "PCC",
        "credits": 3.5,
        "topics": [
            {
                "name": "Regular Languages, DFA, NFA & Pumping Lemma",
                "assignment": "NFA to DFA Subset Construction Problem Set",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [82], "vmahajan1_be24@thapar.edu": [92]},
            },
            {
                "name": "Context-Free Grammars & Pushdown Automata",
                "assignment": "Chomsky Normal Form & CKY Parser Design",
                "due_days": 15,
                "scores": {"kkhushi1_be24@thapar.edu": [76], "sgarg6_be24@thapar.edu": [80]},
            },
            {
                "name": "Turing Machines & Decidability",
                "assignment": "Halting Problem & Universal Turing Machine Spec",
                "due_days": 24,
                "scores": {"ugautam_be24@thapar.edu": [85], "vmahajan1_be24@thapar.edu": [94]},
            },
        ],
    },
    {
        "code": "UMA071",
        "name": "Numerical Optimization",
        "semester": 6,
        "category": "ESC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Linear Programming & Simplex Method",
                "assignment": "Simplex Duality and Branch-and-Bound Solver",
                "due_days": 9,
                "scores": {"ugautam_be24@thapar.edu": [80], "vmahajan1_be24@thapar.edu": [88]},
            },
            {
                "name": "Unconstrained Search & Gradient Techniques",
                "assignment": "Conjugate Gradient & Quasi-Newton Optimization",
                "due_days": 18,
                "scores": {"kkhushi1_be24@thapar.edu": [74], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Constrained Optimization & KKT Conditions",
                "assignment": "Support Vector Machine Formulation via KKT",
                "due_days": 26,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [90]},
            },
        ],
    },
    {
        "code": "UTA025",
        "name": "Innovation and Entrepreneurship",
        "semester": 6,
        "category": "PRJ",
        "credits": 3.0,
        "topics": [
            {
                "name": "Entrepreneurial Opportunity Identification",
                "assignment": "Problem Discovery & Prototype Reverse Engineering",
                "due_days": 12,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [92]},
            },
            {
                "name": "Business Model Canvas & Lean Startup",
                "assignment": "Value Proposition Design & Investor Pitch Deck",
                "due_days": 23,
                "scores": {"kkhushi1_be24@thapar.edu": [95], "sgarg6_be24@thapar.edu": [88]},
            },
        ],
    },

    # ── SEMESTER VII ───────────────────────────────────────────
    {
        "code": "UCS802",
        "name": "Compiler Construction",
        "semester": 7,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Lexical Analysis & Syntax Analysis (LEX/YACC)",
                "assignment": "SLR Parser & Abstract Syntax Tree Generator",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [84], "vmahajan1_be24@thapar.edu": [90]},
            },
            {
                "name": "Intermediate Code Generation & Type Checking",
                "assignment": "Three-Address Code Generation from AST",
                "due_days": 16,
                "scores": {"kkhushi1_be24@thapar.edu": [78], "sgarg6_be24@thapar.edu": [82]},
            },
            {
                "name": "Code Optimization & Target Code Generation",
                "assignment": "Basic Block Optimization & Sethi-Ullman Register Allocation",
                "due_days": 25,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [92]},
            },
        ],
    },
    {
        "code": "UHU005",
        "name": "Humanities for Engineers",
        "semester": 7,
        "category": "HSS",
        "credits": 3.0,
        "topics": [
            {
                "name": "Human Values, Ethics & Organizational Behavior",
                "assignment": "Corporate Whistle-Blowing Case Study Analysis",
                "due_days": 11,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [94]},
            },
            {
                "name": "Managerial Economics, Game Theory & Capital Budgeting",
                "assignment": "Nash Equilibrium & NPV Financial Evaluation",
                "due_days": 22,
                "scores": {"kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [86]},
            },
        ],
    },
    {
        "code": "UCS714",
        "name": "Agentic AI",
        "semester": 7,
        "category": "PCC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Foundations of Generative & Agentic AI",
                "assignment": "Comparison Analysis of Autonomous LLM Agent Frameworks",
                "due_days": 4,
                "scores": {"ugautam_be24@thapar.edu": [94], "vmahajan1_be24@thapar.edu": [90], "kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [92]},
            },
            {
                "name": "Prompt Engineering & Reasoning Strategies",
                "assignment": "ReAct & Chain-of-Thought Prompt Optimization Pipeline",
                "due_days": 10,
                "scores": {"ugautam_be24@thapar.edu": [96], "vmahajan1_be24@thapar.edu": [92], "kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [95]},
            },
            {
                "name": "Agent Architectures, Tools & Task Decomposition",
                "assignment": "Autonomous Tool-Using Agent with Memory and State",
                "due_days": 18,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [88], "kkhushi1_be24@thapar.edu": [85], "sgarg6_be24@thapar.edu": [91]},
            },
            {
                "name": "Collaborative Multi-Agent Systems & MCP Orchestration",
                "assignment": "Multi-Agent DAG Workflow using Model Context Protocol",
                "due_days": 27,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [86], "kkhushi1_be24@thapar.edu": [84], "sgarg6_be24@thapar.edu": [90]},
            },
        ],
    },

    # ── SEMESTER VIII ──────────────────────────────────────────
    {
        "code": "UCS813",
        "name": "Social Network Analysis",
        "semester": 8,
        "category": "PCC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Network Centrality & Graph Models",
                "assignment": "PageRank and Community Detection on Social Graphs",
                "due_days": 10,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [92]},
            },
            {
                "name": "Link Prediction & Information Cascades",
                "assignment": "Relational Bayesian Network Link Prediction",
                "due_days": 21,
                "scores": {"kkhushi1_be24@thapar.edu": [82], "sgarg6_be24@thapar.edu": [84]},
            },
        ],
    },
    {
        "code": "UCS806",
        "name": "Ethical Hacking",
        "semester": 8,
        "category": "PCC",
        "credits": 4.0,
        "topics": [
            {
                "name": "Footprinting, Reconnaissance & Network Scanning",
                "assignment": "Nmap Scanning & Vulnerability Assessment Lab",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [88], "vmahajan1_be24@thapar.edu": [80]},
            },
            {
                "name": "System Hacking, Sniffing & Session Hijacking",
                "assignment": "ARP Spoofing & Wireshark Traffic Inspection",
                "due_days": 16,
                "scores": {"kkhushi1_be24@thapar.edu": [92], "sgarg6_be24@thapar.edu": [90]},
            },
            {
                "name": "Web Application Security & Cryptographic Auditing",
                "assignment": "SQL Injection & Cross-Site Scripting (XSS) Mitigation",
                "due_days": 26,
                "scores": {"ugautam_be24@thapar.edu": [94], "vmahajan1_be24@thapar.edu": [85]},
            },
        ],
    },

    # ── ELECTIVE FOCUS BASKETS ─────────────────────────────────
    {
        "code": "UCS531",
        "name": "Cloud Computing",
        "semester": 5,
        "category": "PEC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Cloud Architecture & AWS Services (EC2, S3)",
                "assignment": "RESTful Web Service Deployment on Cloud VM",
                "due_days": 9,
                "scores": {"ugautam_be24@thapar.edu": [90], "vmahajan1_be24@thapar.edu": [85]},
            },
            {
                "name": "Virtualization, Server Consolidation & Green Data Centers",
                "assignment": "Virtualization Energy Efficiency & Carbon Footprint Audit",
                "due_days": 19,
                "scores": {"kkhushi1_be24@thapar.edu": [88], "sgarg6_be24@thapar.edu": [84]},
            },
        ],
    },
    {
        "code": "UCS534",
        "name": "Computer & Network Security",
        "semester": 5,
        "category": "PEC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Vulnerabilities, Shellshock & Buffer Overflow",
                "assignment": "Stack Layout Analysis & Buffer Overflow Exploit",
                "due_days": 7,
                "scores": {"ugautam_be24@thapar.edu": [86], "vmahajan1_be24@thapar.edu": [78]},
            },
            {
                "name": "Firewalls, IPTables & Transport Layer Security",
                "assignment": "Stateful Firewall Configuration & TLS Handshake Inspection",
                "due_days": 21,
                "scores": {"kkhushi1_be24@thapar.edu": [94], "sgarg6_be24@thapar.edu": [89]},
            },
        ],
    },
    {
        "code": "UCS660",
        "name": "Continuous Integration and Continuous Deployment",
        "semester": 6,
        "category": "PEC",
        "credits": 3.0,
        "topics": [
            {
                "name": "DevOps Automation & CI/CD Pipeline Anatomy",
                "assignment": "Jenkins Multi-Stage Automated Build & Test Pipeline",
                "due_days": 8,
                "scores": {"ugautam_be24@thapar.edu": [92], "vmahajan1_be24@thapar.edu": [88]},
            },
            {
                "name": "Automated Testing, TDD & Code Refactoring",
                "assignment": "JUnit Test Suite with Continuous Feedback & Coverage",
                "due_days": 20,
                "scores": {"kkhushi1_be24@thapar.edu": [86], "sgarg6_be24@thapar.edu": [90]},
            },
        ],
    },
    {
        "code": "UCS748",
        "name": "Generative AI",
        "semester": 7,
        "category": "PEC",
        "credits": 3.0,
        "topics": [
            {
                "name": "Large Language Models & Transformer Architecture",
                "assignment": "Pre-Training vs Fine-Tuning LLMs on Domain Dataset",
                "due_days": 6,
                "scores": {"ugautam_be24@thapar.edu": [95], "vmahajan1_be24@thapar.edu": [91]},
            },
            {
                "name": "Text/Image Generation & Prompt Engineering",
                "assignment": "Chain-of-Thought & Tree-of-Thought Implementation",
                "due_days": 18,
                "scores": {"kkhushi1_be24@thapar.edu": [90], "sgarg6_be24@thapar.edu": [94]},
            },
        ],
    },
]
