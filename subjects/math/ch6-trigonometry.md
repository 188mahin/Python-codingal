# Chapter 6: Further Trigonometry

## 6️⃣ Overview
This chapter extends trigonometry beyond right-angled triangles. It covers sine and cosine rules, obtuse angles, and finding areas of triangles using trigonometric methods.

---

## 📋 Topics Covered

1. Sine and cosine of obtuse angles
2. Area of a triangle using trigonometry
3. Sine rule
4. Cosine rule
5. Solving triangles

---

## 🔑 Key Formulas

### Sine and Cosine of Obtuse Angles

For an obtuse angle A (90° < A < 180°):

```
sin A = sin(180° - A)
cos A = -cos(180° - A)
tan A = -tan(180° - A)
```

**Explanation**: 
- Sine is POSITIVE for obtuse angles
- Cosine is NEGATIVE for obtuse angles
- These angles are supplementary (sum to 180°)

**Examples**:
```
sin 150° = sin(180° - 150°) = sin 30° = 0.5
cos 150° = -cos(180° - 150°) = -cos 30° = -√3/2
```

---

### Area of a Triangle

```
Area = ½ab sin C
     = ½bc sin A
     = ½ac sin B
```

Where a, b, c are sides and A, B, C are the opposite angles.

**When to use**: When you know 2 sides and the included angle (SAS)

**Example**:
```
Triangle ABC: a = 5 cm, b = 7 cm, angle C = 40°

Area = ½ × 5 × 7 × sin 40°
     = ½ × 5 × 7 × 0.6428
     = 11.25 cm²
```

---

### Sine Rule

```
a/sin A = b/sin B = c/sin C

Equivalently: sin A/a = sin B/b = sin C/c
```

Where a, b, c are sides opposite to angles A, B, C respectively.

**When to use**:
- When you know 2 angles + 1 side (AAS or ASA)
- When you know 2 sides + 1 non-included angle (SSA)

**Example 1 - Finding a side**:
```
Triangle ABC: angle A = 40°, angle B = 60°, side a = 5 cm
Find side b.

b/sin B = a/sin A
b/sin 60° = 5/sin 40°
b = (5 × sin 60°)/sin 40°
b = (5 × 0.866)/0.643
b ≈ 6.73 cm
```

**Example 2 - Finding an angle**:
```
Triangle ABC: a = 8 cm, b = 6 cm, angle A = 50°
Find angle B.

sin B/b = sin A/a
sin B/6 = sin 50°/8
sin B = (6 × sin 50°)/8
sin B = (6 × 0.766)/8
sin B ≈ 0.575
B ≈ 35.1° or B ≈ 144.9°
```

---

### ⚠️ Ambiguous Case (SSA)

When given 2 sides and a non-included angle, there may be **0, 1, or 2** valid triangles.

**Example**:
```
Given: a = 3, b = 4, angle A = 30°

sin B/4 = sin 30°/3
sin B = (4 × 0.5)/3 = 2/3 ≈ 0.667

B ≈ 41.8° or B ≈ 138.2°

Both are valid! (Check if sum of angles < 180°)
```

---

### Cosine Rule

```
a² = b² + c² - 2bc cos A
b² = a² + c² - 2ac cos B
c² = a² + b² - 2ab cos C
```

**To find an angle** (rearranged):
```
cos A = (b² + c² - a²)/(2bc)
cos B = (a² + c² - b²)/(2ac)
cos C = (a² + b² - c²)/(2ab)
```

**When to use**:
- When you know all 3 sides (SSS) - find an angle
- When you know 2 sides + included angle (SAS) - find the third side

**Example 1 - Finding a side**:
```
Triangle ABC: b = 5 cm, c = 7 cm, angle A = 50°

a² = 5² + 7² - 2(5)(7)cos 50°
a² = 25 + 49 - 70 × 0.643
a² = 74 - 45.0
a² = 29
a ≈ 5.39 cm
```

**Example 2 - Finding an angle**:
```
Triangle ABC: a = 5 cm, b = 6 cm, c = 7 cm

cos A = (6² + 7² - 5²)/(2 × 6 × 7)
cos A = (36 + 49 - 25)/84
cos A = 60/84
cos A ≈ 0.714
A ≈ 44.4°
```

---

## 📊 Decision Tree: Which Rule to Use?

```
Given information?

├─ 2 angles + 1 side → USE SINE RULE
├─ 2 sides + included angle → USE COSINE RULE or AREA formula
├─ 2 sides + non-included angle → USE SINE RULE (watch for ambiguous case)
└─ 3 sides → USE COSINE RULE to find angles
```

---

## 🎯 Worked Examples

### Example 1: Sine Rule (Finding a Side)
```
In triangle ABC, angle A = 35°, angle B = 75°, side a = 8 m.
Find side b.

Solution:
b/sin B = a/sin A
b/sin 75° = 8/sin 35°
b = (8 × sin 75°)/sin 35°
b = (8 × 0.9659)/0.5736
b ≈ 13.46 m
```

---

### Example 2: Cosine Rule (Finding a Side)
```
In triangle PQR, p = 4 cm, q = 6 cm, angle R = 50°.
Find side r.

Solution:
r² = p² + q² - 2pq cos R
r² = 4² + 6² - 2(4)(6)cos 50°
r² = 16 + 36 - 48 × 0.6428
r² = 52 - 30.85
r² = 21.15
r ≈ 4.60 cm
```

---

### Example 3: Area of Triangle
```
Triangle XYZ has sides x = 9 cm, y = 12 cm, and angle Z = 35°.
Find the area.

Solution:
Area = ½xy sin Z
Area = ½ × 9 × 12 × sin 35°
Area = 54 × 0.5736
Area ≈ 30.97 cm²
```

---

### Example 4: Finding an Angle (Cosine Rule)
```
Triangle ABC has sides a = 7 cm, b = 8 cm, c = 10 cm.
Find angle A.

Solution:
cos A = (b² + c² - a²)/(2bc)
cos A = (64 + 100 - 49)/(2 × 8 × 10)
cos A = 115/160
cos A = 0.71875
A ≈ 44.0°
```

---

## ✅ Exam Tips

1. **Always sketch the triangle** - label sides and angles
2. **Identify which information you have** - then choose the correct rule
3. **Watch for obtuse angles** - remember cos is negative
4. **For SSA cases** - check if there could be 2 solutions
5. **Show all working** - including substitution into the formula
6. **Use calculator correctly** - ensure it's in DEGREE mode
7. **State the rule used** - write "By Sine Rule" or "By Cosine Rule"
8. **Check reasonableness** - do the sides match the angles?

---

## 📈 Summary Table

| Given | Formula | When to Use |
|-------|---------|------------|
| 2 angles + 1 side | Sine rule | AAS or ASA |
| 2 sides + included angle | Cosine rule | SAS |
| 2 sides + non-included angle | Sine rule | SSA (check ambiguity) |
| 3 sides | Cosine rule | SSS |
| 2 sides + included angle | Area = ½ab sin C | Finding area |

---

## 📝 Practice Questions

Try solving these:
1. In triangle ABC, angle A = 45°, angle B = 65°, side a = 10 cm. Find side b.
2. In triangle PQR, p = 7 cm, q = 9 cm, angle R = 40°. Find r.
3. Find the area of triangle XYZ with x = 5 cm, y = 8 cm, angle Z = 50°.
4. In triangle ABC, a = 6 cm, b = 8 cm, c = 10 cm. Find angle B.
5. In triangle ABC, angle A = 30°, angle B = 50°, side b = 12 cm. Find side a.

---

**Previous Chapter**: [Chapter 4: Coordinate Geometry](../ch4-coordinate-geometry.md)  
**Next Chapter**: [Chapter 7: Applications of Trigonometry](./ch7-trig-applications.md)  
**Back to Overview**: [Mathematics Home](./README.md)
