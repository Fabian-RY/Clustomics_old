USE clustomics;

INSERT INTO user_info (username, email, pass) VALUES ('test_user', 'test@clustomics.com', 'patata');
INSERT INTO groups (group_name, max_users_number) VALUES('test_group', 8);
INSERT INTO member_group (username, group_name, admin) VALUES ('test_user', 'test_group', true);

