# Input: 
# Person table:
# +----------+----------+-----------+
# | personId | lastName | firstName |
# +----------+----------+-----------+
# | 1        | Wang     | Allen     |
# | 2        | Alice    | Bob       |
# +----------+----------+-----------+
# Address table:
# +-----------+----------+---------------+------------+
# | addressId | personId | city          | state      |
# +-----------+----------+---------------+------------+
# | 1         | 2        | New York City | New York   |
# | 2         | 3        | Leetcode      | California |
# +-----------+----------+---------------+------------+
# Output: 
# +-----------+----------+---------------+----------+
# | firstName | lastName | city          | state    |
# +-----------+----------+---------------+----------+
# | Allen     | Wang     | Null          | Null     |
# | Bob       | Alice    | New York City | New York |
# +-----------+----------+---------------+----------+



#Solution 

SELECT p.firstName, p.lastName, a.city, a.state FROM 
Person p LEFT JOIN Address a ON p.personId = a.personId



# Alternatively

SELECT p.firstName, p.lastName, a.city, a.state FROM 
Person p LEFT JOIN Address a USING (personId)