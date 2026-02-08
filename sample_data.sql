TRUNCATE TABLE RESOURCE_AVAILABILITY,
RESOURCE_SKILL,
TASKS,
RESOURCES,
SKILLS,
PROJECTS RESTART IDENTITY CASCADE;

INSERT INTO
	SKILLS (ID, NAME)
VALUES
	(1, 'NodeJS'),
	(2, 'SQL'),
	(3, 'Python');

INSERT INTO
	PROJECTS (ID, NAME)
VALUES
	(1, 'ERP'),
	(2, 'Data Pipelines');

INSERT INTO
	RESOURCES (ID, NAME)
VALUES
	(1, 'Aravind'),
	(2, 'Akash'),
	(3, 'Karthi'),
	(4, 'Dharani');

INSERT INTO
	RESOURCE_SKILL (RESOURCE_ID, SKILL_ID)
VALUES
	(1, 3),
	(1, 2),
	(2, 1),
	(3, 2),
	(4, 3);

INSERT INTO
	TASKS (
		ID,
		PROJECT_ID,
		SKILL_ID,
		NAME,
		START_DATE,
		END_DATE
	)
VALUES
	(
		1,
		1,
		1,
		'Implement a microservice to fetch daily weather data',
		'2024-02-01',
		'2024-02-05'
	),
	(
		2,
		1,
		2,
		'Create Trigger functions for data_pipeline table',
		'2024-02-03',
		'2024-02-07'
	),
	(
		3,
		1,
		1,
		'Add testcases to existing microservices',
		'2024-02-03',
		'2024-02-06'
	),
	(
		4,
		2,
		3,
		'Create an automation for sending slack messages',
		'2024-02-01',
		'2024-02-04'
	),
	(
		5,
		1,
		2,
		'Run migration on customer_analytics table',
		'2024-02-01',
		'2024-02-04'
	);

INSERT INTO
	RESOURCE_AVAILABILITY (RESOURCE_ID, AVAILABLE_FROM, AVAILABLE_TO)
VALUES
	(1, '2024-02-01', '2024-02-08'),
	(2, '2024-02-02', '2024-02-07'),
	(3, '2024-02-01', '2024-02-04'),
	(3, '2024-02-08', '2024-02-10'),
	(4, '2024-02-01', '2024-02-10');