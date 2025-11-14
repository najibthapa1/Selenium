CREATE TABLE claimfile (
    Id INT PRIMARY KEY,
    UserId UUID,
    ClaimType VARCHAR(50),
    ClaimValue TEXT
);

COPY claimfile (Id, UserId, ClaimType, ClaimValue)
FROM '/Users/najibthapa1/Documents/project/pythonProject/kfPivot/claimsfile.csv'
DELIMITER ','
CSV HEADER;

select * from claimfile 
where UserId='14666c7a-6aba-424e-bb4b-c3e9ab809fa3'
and ClaimType in ('UserName','Name','BranchName','Designation','Department');

SELECT UserId, 
       MAX(CASE WHEN ClaimType = 'userName' THEN ClaimValue END) AS "UserName",
       MAX(CASE WHEN ClaimType = 'name' THEN ClaimValue END) AS "Name",
       MAX(CASE WHEN ClaimType = 'branchName' THEN ClaimValue END) AS "BranchName",
       MAX(CASE WHEN ClaimType = 'designation' THEN ClaimValue END) AS "Designation",
       MAX(CASE WHEN ClaimType = 'department' THEN ClaimValue END) AS "Department"
FROM claimfile
WHERE --UserId = '14666c7a-6aba-424e-bb4b-c3e9ab809fa3'
--AND 
ClaimType IN ('userName', 'name', 'branchName', 'designation', 'department')
GROUP BY UserId;