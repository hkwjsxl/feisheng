-- 如果使用数据库本身的外键，则添加/删除/修改数据时，务必关闭原来表中的主外键约束功能
set FOREIGN_KEY_CHECKS = 0;

-- 清空原有的课程信息表信息
truncate table fs_course_info;

-- 添加课程信息
INSERT INTO fs.fs_course_info (id, name, orders, is_show, is_deleted, created_time, updated_time, course_cover,
                               course_video, course_type, level, description, pub_date, period, attachment_path,
                               attachment_link, status, students, lessons, pub_lessons, price, recomment_home_hot,
                               recomment_home_top, category_id, direction_id, teacher_id)
VALUES (1, '7天Typescript从入门到放弃', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871',
        'course/cover/course-10.png', '', 0, 0, '<p>7天Typescript从入门到放弃</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip',
        null, 0, 988, 100, 30, 998.00, 1, 1, 2, 1, 1),
       (2, '3天Typescript精修', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871',
        'course/cover/course-9.png', '', 0, 0, '<p>3天Typescript精修</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip',
        null, 0, 988, 100, 30, 998.00, 1, 1, 2, 1, 1),
       (3, '3天学会Vue基础', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871',
        'course/cover/course-8.png', '', 0, 0, '<p>3天学会Vue基础</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0,
        988, 100, 30, 998.00, 1, 1, 2, 1, 1);

-- 如果使用数据库本身的外键，则添加/删除/修改数据以后，务必开启原来表中的主外键约束功能
set FOREIGN_KEY_CHECKS = 1;