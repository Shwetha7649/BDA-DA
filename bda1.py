# Given dataset
dataset = """
1,John,Engineering
2,Jane,Commerce
3,Tom,Arts
4,Lucy,Engineering
5,Anna,Commerce
6,Mark,Arts
7,Emma,Engineering
8,James,Commerce
9,Sophia,Arts
10,Michael,Engineering
11,Alice,Commerce
12,David,Arts
13,Olivia,Engineering
14,William,Commerce
15,Isabella,Arts
16,Daniel,Engineering
17,Charlotte,Commerce
18,Matthew,Arts
19,Ethan,Engineering
20,Ava,Commerce
21,Jackson,Arts
22,Amelia,Engineering
23,Noah,Commerce
24,Harper,Arts
25,Lucas,Engineering
26,Elizabeth,Commerce
27,Logan,Arts
28,Grace,Engineering
29,Benjamin,Commerce
30,Lily,Arts
31,Alexander,Engineering
32,Mia,Commerce
33,Henry,Arts
34,Chloe,Engineering
35,Jacob,Commerce
36,Zoey,Arts
37,Elijah,Engineering
38,Emily,Commerce
39,James,Arts
40,Oliver,Engineering
41,Aria,Commerce
42,Jack,Arts
43,Samantha,Engineering
44,Jackson,Commerce
45,Abigail,Arts
46,Michael,Engineering
47,Charlotte,Commerce
48,Daniel,Arts
49,Eleanor,Engineering
50,James,Commerce
51,Luna,Arts
52,Matthew,Engineering
53,Avery,Commerce
54,Leo,Arts
55,Emily,Engineering
56,Henry,Commerce
57,Scarlett,Arts
58,Jack,Engineering
59,Harper,Commerce
60,Oliver,Arts
61,Chloe,Engineering
62,Liam,Commerce
63,Emma,Arts
64,Sophia,Engineering
65,Jacob,Commerce
66,Isabella,Arts
67,William,Engineering
68,Ava,Commerce
69,Logan,Arts
70,James,Engineering
71,Mia,Commerce
72,Noah,Arts
73,Olivia,Engineering
74,Luke,Commerce
75,Eleanor,Arts
76,Grace,Engineering
77,Leo,Commerce
78,Charlotte,Arts
79,Avery,Engineering
80,David,Commerce
81,Sophia,Arts
82,Jackson,Engineering
83,Aria,Commerce
84,Emma,Arts
85,Michael,Engineering
86,Lily,Commerce
87,Olivia,Arts
88,James,Engineering
89,Isabella,Commerce
90,Mia,Arts
91,Henry,Engineering
92,Avery,Commerce
93,Lucas,Arts
94,Elizabeth,Engineering
95,Grace,Commerce
96,Oliver,Arts
97,Emily,Engineering
98,Matthew,Commerce
99,Chloe,Arts
100,Harper,Engineering
101,Jack,Commerce
102,Charlotte,Arts
103,Eleanor,Engineering
104,Luna,Commerce
105,Noah,Arts
106,James,Engineering
107,Ava,Commerce
108,Olivia,Arts
109,David,Engineering
110,Mia,Commerce
111,Lucas,Arts
112,Emma,Engineering
113,Henry,Commerce
114,Sophia,Arts
115,Olivia,Engineering
116,Jackson,Commerce
117,Chloe,Arts
118,Michael,Engineering
119,Grace,Commerce
120,Avery,Arts
121,Jack,Engineering
122,Isabella,Commerce
123,Emma,Arts
124,Henry,Engineering
125,Luna,Commerce
126,Olivia,Arts
127,Eleanor,Engineering
128,Ava,Commerce
129,Noah,Arts
130,Sophia,Engineering
131,Chloe,Commerce
132,James,Arts
133,Emily,Engineering
134,Lily,Commerce
135,David,Arts
136,Harper,Engineering
137,Jack,Commerce
138,Olivia,Arts
139,Lucas,Engineering
140,Avery,Commerce
141,Charlotte,Arts
142,Noah,Engineering
143,Mia,Commerce
144,Emma,Arts
145,James,Engineering
146,Grace,Commerce
147,Oliver,Arts
148,Eleanor,Engineering
149,Harper,Commerce
150,Sophia,Arts
151,David,Engineering
152,Luna,Commerce
153,Michael,Arts
154,Olivia,Engineering
155,Isabella,Commerce
156,Emma,Arts
157,Avery,Engineering
158,Jack,Commerce
159,Henry,Arts
160,Lily,Engineering
161,Chloe,Commerce
162,Mia,Arts
163,Lucas,Engineering
164,Sophia,Commerce
165,Charlotte,Arts
166,David,Engineering
167,Noah,Commerce
168,Olivia,Arts
169,Emma,Engineering
170,James,Commerce
171,Avery,Arts
172,Jack,Engineering
173,Eleanor,Commerce
174,Michael,Arts
175,Sophia,Engineering
176,Harper,Commerce
177,Chloe,Arts
178,Olivia,Engineering
179,Luna,Commerce
180,Grace,Arts
181,Lucas,Engineering
182,Emma,Commerce
183,Charlotte,Arts
184,James,Engineering
185,Harper,Commerce
186,David,Arts
187,Olivia,Engineering
188,Avery,Commerce
189,Michael,Arts
190,Sophia,Engineering
191,Lily,Commerce
192,Emma,Arts
193,Chloe,Engineering
194,Noah,Commerce
195,Grace,Arts
196,Isabella,Engineering
197,Jack,Commerce
198,Olivia,Arts
199,Henry,Engineering
200,David,Commerce
"""

# Convert dataset to list of strings
people = [line.strip() for line in dataset.strip().split('\n')]

# Map Phase
def map_function(data):
    mapped = []
    for line in data:
        _, person_name, subject = line.split(',')
        mapped.append((subject, 1))
    return mapped

# Reduce Phase
def reduce_function(mapped_data):
    reduced = {}
    for key, value in mapped_data:
        if key in reduced:
            reduced[key] += value
        else:
            reduced[key] = value
    return reduced

# Execute MapReduce
mapped_data = map_function(people)
reduced_data = reduce_function(mapped_data)

# Display Results
print("Subject counts:")
for subject, count in reduced_data.items():
    print(f"Subject: {subject}, Count: {count}")