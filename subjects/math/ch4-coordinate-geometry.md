# Chapter 4: Coordinate Geometry

## 4️⃣ Overview
Coordinate geometry (also called analytic geometry) uses algebra to study geometric properties. This chapter focuses on points, lines, gradients, and equations of straight lines in the 2D coordinate plane.

---

## 📋 Topics Covered

1. Length of a line segment
2. Gradient (slope) of a straight line
3. Equation of a straight line
4. Parallel and perpendicular lines
5. Midpoint formula

---

## 🔑 Key Formulas

### Distance Between Two Points (Length of Line Segment)
```
For points A(x₁, y₁) and B(x₂, y₂):

d = √[(x₂ - x₁)² + (y₂ - y₁)²]
```

**Explanation**: This is Pythagoras' theorem applied to coordinates.

**Example**:
```
Find distance between A(2, 3) and B(5, 7)

d = √[(5-2)² + (7-3)²]
d = √[3² + 4²]
d = √[9 + 16]
d = √25
d = 5 units
```

---

### Gradient (Slope) of a Line
```
For points A(x₁, y₁) and B(x₂, y₂):

m = (y₂ - y₁) / (x₂ - x₁)
```

**Explanation**: Gradient = "Rise over Run" = vertical change ÷ horizontal change

**Example**:
```
Find gradient of line through A(1, 2) and B(4, 8)

m = (8 - 2) / (4 - 1)
m = 6 / 3
m = 2
```

### Gradient Interpretation:
- **m > 0**: Line slopes upward (from left to right) ⬆️
- **m < 0**: Line slopes downward (from left to right) ⬇️
- **m = 0**: Horizontal line (parallel to x-axis)
- **m = undefined**: Vertical line (parallel to y-axis)

---

### Midpoint Formula
```
For points A(x₁, y₁) and B(x₂, y₂):

Midpoint M = ((x₁ + x₂)/2, (y₁ + y₂)/2)
```

**Example**:
```
Find midpoint of A(2, 4) and B(8, 10)

M = ((2+8)/2, (4+10)/2)
M = (10/2, 14/2)
M = (5, 7)
```

---

## 📐 Equation of a Straight Line

### Form 1: Slope-Intercept Form
```
y = mx + c
```

Where:
- **m** = gradient
- **c** = y-intercept (where line crosses y-axis)

**Example**:
```
y = 2x + 3
- Gradient = 2
- y-intercept = 3 (point (0, 3))
```

---

### Form 2: Point-Slope Form
```
y - y₁ = m(x - x₁)
```

Use when you know:
- The gradient **m**
- A point **(x₁, y₁)** on the line

**Example**:
```
Find equation of line with gradient 3 through point (2, 5)

y - 5 = 3(x - 2)
y - 5 = 3x - 6
y = 3x - 1
```

---

### Form 3: General Form
```
ax + by + c = 0
```

Used in more advanced applications.

**Example**:
```
Convert y = 2x + 3 to general form

y = 2x + 3
-2x + y - 3 = 0
or
2x - y + 3 = 0
```

---

## 🔗 Finding the Equation of a Line

### Case 1: Given gradient and y-intercept
**Use y = mx + c directly**

```
Example: m = 5, c = -2
Answer: y = 5x - 2
```

---

### Case 2: Given gradient and a point
**Use point-slope form: y - y₁ = m(x - x₁)**

```
Example: m = 3, passes through (1, 4)

y - 4 = 3(x - 1)
y - 4 = 3x - 3
y = 3x + 1
```

---

### Case 3: Given two points
**Step 1**: Find gradient m = (y₂ - y₁)/(x₂ - x₁)
**Step 2**: Use point-slope form with one point

```
Example: Points A(1, 2) and B(4, 8)

Step 1: m = (8-2)/(4-1) = 6/3 = 2

Step 2: Using point A(1, 2)
y - 2 = 2(x - 1)
y - 2 = 2x - 2
y = 2x
```

**Verify with point B**: y = 2(4) = 8 ✓

---

## 📏 Special Lines

### Horizontal Lines
```
Equation: y = k    (where k is a constant)
Gradient: m = 0
Example: y = 5
```

**All points have the same y-coordinate**

---

### Vertical Lines
```
Equation: x = k    (where k is a constant)
Gradient: undefined
Example: x = -3
```

**All points have the same x-coordinate**

---

## 🔄 Parallel and Perpendicular Lines

### Parallel Lines
```
Two lines are parallel if they have the SAME gradient

m₁ = m₂
```

**Example**:
```
Line 1: y = 3x + 2
Line 2: y = 3x - 5

Both have m = 3, so they are parallel
```

---

### Perpendicular Lines
```
Two lines are perpendicular if their gradients multiply to -1

m₁ × m₂ = -1
or
m₂ = -1/m₁
```

**Example**:
```
Line 1: y = 2x + 3  (m₁ = 2)
Line 2 gradient: m₂ = -1/2

So a perpendicular line could be: y = -½x + 5

Check: 2 × (-½) = -1 ✓
```

---

### Finding a Perpendicular Line Through a Point
```
Example: Find line perpendicular to y = 3x + 1 through point (2, 5)

Step 1: Original gradient = 3
Step 2: Perpendicular gradient = -1/3
Step 3: Use point-slope form:
        y - 5 = -⅓(x - 2)
        y - 5 = -⅓x + ⅔
        y = -⅓x + ⅔ + 5
        y = -⅓x + 23/3
```

---

## 📊 Intersection of Two Lines

### Finding the Point of Intersection
**Solve the two equations simultaneously**

```
Example:
Line 1: y = 2x + 1
Line 2: y = -x + 4

Set equal: 2x + 1 = -x + 4
          3x = 3
          x = 1

Substitute: y = 2(1) + 1 = 3

Intersection point: (1, 3)
```

**Verify**: 
- Line 1: y = 2(1) + 1 = 3 ✓
- Line 2: y = -(1) + 4 = 3 ✓

---

## 📈 Summary Table: Common Coordinate Geometry Tasks

| Task | Formula/Method |
|------|-----------------|
| Distance between points | √[(x₂-x₁)² + (y₂-y₁)²] |
| Gradient | (y₂-y₁)/(x₂-x₁) |
| Midpoint | ((x₁+x₂)/2, (y₁+y₂)/2) |
| Equation (m and c) | y = mx + c |
| Equation (m and point) | y - y₁ = m(x - x₁) |
| Parallel lines | m₁ = m₂ |
| Perpendicular lines | m₁ × m₂ = -1 |
| Horizontal line | y = k |
| Vertical line | x = k |

---

## ✅ Exam Tips

1. **Always label your points** clearly as (x₁, y₁) and (x₂, y₂)
2. **Order matters** in the gradient formula - be consistent with subtraction
3. **Show substitution** when finding equations - write the intermediate steps
4. **For perpendicular gradients**, remember: m₂ = -1/m₁ (negative reciprocal)
5. **Check your equation** by substituting back the known points
6. **Watch for vertical lines** - gradient is undefined, not 0
7. **Draw diagrams** when possible - helps visualize the problem

---

## 🧮 Worked Examples

### Example 1: Complete Problem
```
Find the equation of the line perpendicular to y = 2x - 3 
and passing through point (4, -1)

Step 1: Find the perpendicular gradient
Original gradient = 2
Perpendicular gradient = -1/2

Step 2: Use point-slope form with (4, -1)
y - (-1) = -1/2(x - 4)
y + 1 = -1/2 x + 2
y = -1/2 x + 1

Answer: y = -1/2 x + 1  or  x + 2y - 2 = 0
```

---

### Example 2: Finding Intersection
```
Find where y = x + 2 meets y = -2x + 8

x + 2 = -2x + 8
3x = 6
x = 2

y = 2 + 2 = 4

Intersection: (2, 4)
```

---

## 📝 Practice Questions

Try solving these:
1. Find distance between A(-1, 2) and B(3, 5)
2. Find gradient of line through P(2, 8) and Q(5, 2)
3. Write equation of line with gradient 4 and y-intercept -2
4. Find equation of line through (3, 1) and (-1, 5)
5. Find equation of line perpendicular to y = 3x + 2 through (0, 6)
6. Find intersection of y = 2x + 1 and y = -x + 4

---

**Previous Chapter**: [Chapter 3: Indices and Standard Form](./ch3-indices.md)  
**Back to Overview**: [Mathematics Home](./README.md)
