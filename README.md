# Blackholes_Model
My solution to a challenge on py.checkio.com. Not nearly as efficient as some but tried to go down the path of trying to use object oriented processes.

# Link to Challenge
https://py.checkio.org/mission/black-holes/

# Outline of Challenge

"Wow! That was amazing!" Stephen was greatly impressed. He took his eyes off the telescope and leaned back.

"Did you see that?" asked Sofia.

...moments ago a super massive black hole had just "swallowed" another one...

"You were right Sofia, that was an incredible event" Stephen said. "So, can I join your A&A (Astronomy & Astrophysics) research group?"

Sofia looked at him triumphantly and said - "Really, my plan was to rope you in anyway! We are currently researching black holes and their gravitational fields and we are looking for someone to help us create a software model that will predict the future state of black holes".

"Hmm, it's very interesting. Let me try...".

You need to help Stephen implement a software model (function) that predicts the state of black holes under a controlled environment. The A&A research team has identified some peculiarities in the behavior of black holes.

To create the software model one should take into account:

1. The cartesian coordinate system is used to map out the black holes.
2. Each black hole is represented as a circle with x, y (center coordinates) and r (radius).
3. In contrast to the area, which may change during the absorption process, the coordinates remain constant.
4. The area of a black hole greatly influences its mass, and consequently, the gravitational field.
5. The absorption order of black holes depends on the distance between their centers, starting with the black holes that are closest to each other. If the distance between different black holes is equal, then the leftmost black hole in the list should merge first.
6. The absorption process (merging) of black holes is possible if and only if the following conditions are met:
   - The intersection area of the two black holes is greater than or equal to 55% (>= 55%) of one of the two black holes area.
   - The area of one of the two black holes is over 20% (>= 20%) more than the area of the other.
7. If one black hole absorbs another, their areas are summarized as (Stotal = S1 + S2).
8. The absorption process continues as long as all conditions are met (see p. 6).
