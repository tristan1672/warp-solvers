# Differential Operators (3D)

The goal of this folder is to implement the four vector differential operators which are recurring operators in physics equations.

## Gradient ∇ (Nabla / Del)

![alt text](images/grad.png)

Vector of first-order partial derivatives in each axis. Gradient takes a scalar/concentration field and produces a vector field, mapping out how the scalars are spatially distributed across the field. It shows you the direction the values are increasing towards.

Note that the notation shows unit direction vectors, not sum of each derivative, output is a **vector**.

## Divergence

![alt text](images/diverg.png)

Sum of first-order partial derivatives of each directional component of a **vector**. Divergence takes a vector field and produces a scalar field, mapping out the rate the flow is changing across the field. Positive divergence signals an increasing flow which suggests that the volume is expanding and a negative divergence suggests volume is compressing.

Not to be confused with the **Venturi** effect where narrowing space increases _velocity_ of a fluid. Velocity increasing does not equal to positive divergence. Divergence factors in volume differential across space, if an inlet and outlet produces the same volume, divergence is zero.

Note that the output is a **scalar**, sum the derivatives of each directional component together.

## Curl

![alt text](images/curl.png)

## Laplacian Δf or ∇²f

![alt text](images/lap.png)

Sum of second-order partial derivatives
