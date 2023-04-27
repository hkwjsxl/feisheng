/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : fs

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 18/04/2023 15:54:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 125 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 导航菜单', 7, 'add_nav');
INSERT INTO `auth_permission` VALUES (22, 'Can change 导航菜单', 7, 'change_nav');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 导航菜单', 7, 'delete_nav');
INSERT INTO `auth_permission` VALUES (24, 'Can view 导航菜单', 7, 'view_nav');
INSERT INTO `auth_permission` VALUES (25, 'Can add 轮播图', 8, 'add_banner');
INSERT INTO `auth_permission` VALUES (26, 'Can change 轮播图', 8, 'change_banner');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 轮播图', 8, 'delete_banner');
INSERT INTO `auth_permission` VALUES (28, 'Can view 轮播图', 8, 'view_banner');
INSERT INTO `auth_permission` VALUES (29, 'Can add 用户信息', 9, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (30, 'Can change 用户信息', 9, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 用户信息', 9, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (32, 'Can view 用户信息', 9, 'view_userinfo');
INSERT INTO `auth_permission` VALUES (33, 'Can add 课程课时', 10, 'add_courselesson');
INSERT INTO `auth_permission` VALUES (34, 'Can change 课程课时', 10, 'change_courselesson');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 课程课时', 10, 'delete_courselesson');
INSERT INTO `auth_permission` VALUES (36, 'Can view 课程课时', 10, 'view_courselesson');
INSERT INTO `auth_permission` VALUES (37, 'Can add 讲师信息', 11, 'add_teacher');
INSERT INTO `auth_permission` VALUES (38, 'Can change 讲师信息', 11, 'change_teacher');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 讲师信息', 11, 'delete_teacher');
INSERT INTO `auth_permission` VALUES (40, 'Can view 讲师信息', 11, 'view_teacher');
INSERT INTO `auth_permission` VALUES (41, 'Can add 课程分类', 12, 'add_coursecategory');
INSERT INTO `auth_permission` VALUES (42, 'Can change 课程分类', 12, 'change_coursecategory');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 课程分类', 12, 'delete_coursecategory');
INSERT INTO `auth_permission` VALUES (44, 'Can view 课程分类', 12, 'view_coursecategory');
INSERT INTO `auth_permission` VALUES (45, 'Can add 课程章节', 13, 'add_coursechapter');
INSERT INTO `auth_permission` VALUES (46, 'Can change 课程章节', 13, 'change_coursechapter');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 课程章节', 13, 'delete_coursechapter');
INSERT INTO `auth_permission` VALUES (48, 'Can view 课程章节', 13, 'view_coursechapter');
INSERT INTO `auth_permission` VALUES (49, 'Can add 课程信息', 14, 'add_course');
INSERT INTO `auth_permission` VALUES (50, 'Can change 课程信息', 14, 'change_course');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 课程信息', 14, 'delete_course');
INSERT INTO `auth_permission` VALUES (52, 'Can view 课程信息', 14, 'view_course');
INSERT INTO `auth_permission` VALUES (53, 'Can add 学习方向', 15, 'add_coursedirection');
INSERT INTO `auth_permission` VALUES (54, 'Can change 学习方向', 15, 'change_coursedirection');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 学习方向', 15, 'delete_coursedirection');
INSERT INTO `auth_permission` VALUES (56, 'Can view 学习方向', 15, 'view_coursedirection');
INSERT INTO `auth_permission` VALUES (57, 'Can add 优惠活动', 16, 'add_activity');
INSERT INTO `auth_permission` VALUES (58, 'Can change 优惠活动', 16, 'change_activity');
INSERT INTO `auth_permission` VALUES (59, 'Can delete 优惠活动', 16, 'delete_activity');
INSERT INTO `auth_permission` VALUES (60, 'Can view 优惠活动', 16, 'view_activity');
INSERT INTO `auth_permission` VALUES (61, 'Can add 优惠类型', 17, 'add_discounttype');
INSERT INTO `auth_permission` VALUES (62, 'Can change 优惠类型', 17, 'change_discounttype');
INSERT INTO `auth_permission` VALUES (63, 'Can delete 优惠类型', 17, 'delete_discounttype');
INSERT INTO `auth_permission` VALUES (64, 'Can view 优惠类型', 17, 'view_discounttype');
INSERT INTO `auth_permission` VALUES (65, 'Can add 优惠公式', 18, 'add_discount');
INSERT INTO `auth_permission` VALUES (66, 'Can change 优惠公式', 18, 'change_discount');
INSERT INTO `auth_permission` VALUES (67, 'Can delete 优惠公式', 18, 'delete_discount');
INSERT INTO `auth_permission` VALUES (68, 'Can view 优惠公式', 18, 'view_discount');
INSERT INTO `auth_permission` VALUES (69, 'Can add 课程参与活动的价格表', 19, 'add_courseactivityprice');
INSERT INTO `auth_permission` VALUES (70, 'Can change 课程参与活动的价格表', 19, 'change_courseactivityprice');
INSERT INTO `auth_permission` VALUES (71, 'Can delete 课程参与活动的价格表', 19, 'delete_courseactivityprice');
INSERT INTO `auth_permission` VALUES (72, 'Can view 课程参与活动的价格表', 19, 'view_courseactivityprice');
INSERT INTO `auth_permission` VALUES (73, 'Can add 订单记录', 20, 'add_order');
INSERT INTO `auth_permission` VALUES (74, 'Can change 订单记录', 20, 'change_order');
INSERT INTO `auth_permission` VALUES (75, 'Can delete 订单记录', 20, 'delete_order');
INSERT INTO `auth_permission` VALUES (76, 'Can view 订单记录', 20, 'view_order');
INSERT INTO `auth_permission` VALUES (77, 'Can add 订单详情', 21, 'add_orderdetail');
INSERT INTO `auth_permission` VALUES (78, 'Can change 订单详情', 21, 'change_orderdetail');
INSERT INTO `auth_permission` VALUES (79, 'Can delete 订单详情', 21, 'delete_orderdetail');
INSERT INTO `auth_permission` VALUES (80, 'Can view 订单详情', 21, 'view_orderdetail');
INSERT INTO `auth_permission` VALUES (81, 'Can add 优惠券', 22, 'add_coupon');
INSERT INTO `auth_permission` VALUES (82, 'Can change 优惠券', 22, 'change_coupon');
INSERT INTO `auth_permission` VALUES (83, 'Can delete 优惠券', 22, 'delete_coupon');
INSERT INTO `auth_permission` VALUES (84, 'Can view 优惠券', 22, 'view_coupon');
INSERT INTO `auth_permission` VALUES (85, 'Can add 优惠券与学习方向', 23, 'add_coupondirection');
INSERT INTO `auth_permission` VALUES (86, 'Can change 优惠券与学习方向', 23, 'change_coupondirection');
INSERT INTO `auth_permission` VALUES (87, 'Can delete 优惠券与学习方向', 23, 'delete_coupondirection');
INSERT INTO `auth_permission` VALUES (88, 'Can view 优惠券与学习方向', 23, 'view_coupondirection');
INSERT INTO `auth_permission` VALUES (89, 'Can add 优惠券与课程信息', 24, 'add_couponcourse');
INSERT INTO `auth_permission` VALUES (90, 'Can change 优惠券与课程信息', 24, 'change_couponcourse');
INSERT INTO `auth_permission` VALUES (91, 'Can delete 优惠券与课程信息', 24, 'delete_couponcourse');
INSERT INTO `auth_permission` VALUES (92, 'Can view 优惠券与课程信息', 24, 'view_couponcourse');
INSERT INTO `auth_permission` VALUES (93, 'Can add 优惠券发放和使用日志', 25, 'add_couponlog');
INSERT INTO `auth_permission` VALUES (94, 'Can change 优惠券发放和使用日志', 25, 'change_couponlog');
INSERT INTO `auth_permission` VALUES (95, 'Can delete 优惠券发放和使用日志', 25, 'delete_couponlog');
INSERT INTO `auth_permission` VALUES (96, 'Can view 优惠券发放和使用日志', 25, 'view_couponlog');
INSERT INTO `auth_permission` VALUES (97, 'Can add 优惠券与课程分类', 26, 'add_couponcoursecat');
INSERT INTO `auth_permission` VALUES (98, 'Can change 优惠券与课程分类', 26, 'change_couponcoursecat');
INSERT INTO `auth_permission` VALUES (99, 'Can delete 优惠券与课程分类', 26, 'delete_couponcoursecat');
INSERT INTO `auth_permission` VALUES (100, 'Can view 优惠券与课程分类', 26, 'view_couponcoursecat');
INSERT INTO `auth_permission` VALUES (101, 'Can add 积分流水', 27, 'add_credit');
INSERT INTO `auth_permission` VALUES (102, 'Can change 积分流水', 27, 'change_credit');
INSERT INTO `auth_permission` VALUES (103, 'Can delete 积分流水', 27, 'delete_credit');
INSERT INTO `auth_permission` VALUES (104, 'Can view 积分流水', 27, 'view_credit');
INSERT INTO `auth_permission` VALUES (105, 'Can add 用户课程购买记录', 28, 'add_usercourse');
INSERT INTO `auth_permission` VALUES (106, 'Can change 用户课程购买记录', 28, 'change_usercourse');
INSERT INTO `auth_permission` VALUES (107, 'Can delete 用户课程购买记录', 28, 'delete_usercourse');
INSERT INTO `auth_permission` VALUES (108, 'Can view 用户课程购买记录', 28, 'view_usercourse');
INSERT INTO `auth_permission` VALUES (109, 'Can add 问答记录', 29, 'add_studyqa');
INSERT INTO `auth_permission` VALUES (110, 'Can change 问答记录', 29, 'change_studyqa');
INSERT INTO `auth_permission` VALUES (111, 'Can delete 问答记录', 29, 'delete_studyqa');
INSERT INTO `auth_permission` VALUES (112, 'Can view 问答记录', 29, 'view_studyqa');
INSERT INTO `auth_permission` VALUES (113, 'Can add 学习笔记', 30, 'add_studynote');
INSERT INTO `auth_permission` VALUES (114, 'Can change 学习笔记', 30, 'change_studynote');
INSERT INTO `auth_permission` VALUES (115, 'Can delete 学习笔记', 30, 'delete_studynote');
INSERT INTO `auth_permission` VALUES (116, 'Can view 学习笔记', 30, 'view_studynote');
INSERT INTO `auth_permission` VALUES (117, 'Can add 代码记录', 31, 'add_studycode');
INSERT INTO `auth_permission` VALUES (118, 'Can change 代码记录', 31, 'change_studycode');
INSERT INTO `auth_permission` VALUES (119, 'Can delete 代码记录', 31, 'delete_studycode');
INSERT INTO `auth_permission` VALUES (120, 'Can view 代码记录', 31, 'view_studycode');
INSERT INTO `auth_permission` VALUES (121, 'Can add 课时进度记录', 32, 'add_studyprogress');
INSERT INTO `auth_permission` VALUES (122, 'Can change 课时进度记录', 32, 'change_studyprogress');
INSERT INTO `auth_permission` VALUES (123, 'Can delete 课时进度记录', 32, 'delete_studyprogress');
INSERT INTO `auth_permission` VALUES (124, 'Can view 课时进度记录', 32, 'view_studyprogress');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_fs_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_fs_user_id` FOREIGN KEY (`user_id`) REFERENCES `fs_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2023-03-22 15:46:10.358144', '5', 'alex', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (2, '2023-03-22 15:54:32.899852', '5', 'alex', 2, '[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (3, '2023-03-22 15:54:57.086319', '4', '红老师', 2, '[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (4, '2023-03-22 15:55:05.135915', '5', 'alex', 2, '[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (5, '2023-03-22 15:55:13.069672', '5', 'alex', 2, '[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (6, '2023-03-22 15:55:37.054670', '5', 'alex', 3, '', 11, 1);
INSERT INTO `django_admin_log` VALUES (7, '2023-03-22 16:44:23.763570', '2', 'username---18533538211', 2, '[]', 9, 1);
INSERT INTO `django_admin_log` VALUES (8, '2023-03-22 16:48:12.299769', '2', 'username---18533538211', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (9, '2023-04-02 13:34:49.276685', '20', 'Redis入门课程', 2, '[{\"changed\": {\"fields\": [\"\\u5b66\\u4e60\\u4eba\\u6570\"]}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (10, '2023-04-02 13:34:56.626376', '20', 'Redis入门课程', 2, '[{\"changed\": {\"fields\": [\"\\u5c01\\u9762\\u89c6\\u9891\"]}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (11, '2023-04-07 12:15:50.937883', '12', 'CouponLog object (12)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (12, '2023-04-07 12:15:59.602731', '11', 'CouponLog object (11)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (13, '2023-04-07 12:16:03.737060', '10', 'CouponLog object (10)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (14, '2023-04-07 12:16:05.959785', '9', 'CouponLog object (9)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (15, '2023-04-07 12:16:09.611170', '8', 'CouponLog object (8)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (16, '2023-04-07 12:16:12.452825', '5', 'CouponLog object (5)', 2, '[]', 25, 1);
INSERT INTO `django_admin_log` VALUES (17, '2023-04-08 16:43:04.971856', '1', 'username---root', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\", \"Last login\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (18, '2023-04-08 16:45:59.444295', '1', 'username---root', 2, '[{\"changed\": {\"fields\": [\"\\u79ef\\u5206\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (19, '2023-04-08 16:46:11.880829', '1', 'username---root', 2, '[{\"changed\": {\"fields\": [\"\\u79ef\\u5206\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (20, '2023-04-08 16:48:03.461824', '2', 'username---18533538211', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (21, '2023-04-08 16:48:26.382398', '2', 'username---18533538211', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (22, '2023-04-08 16:48:26.421400', '3', 'username---18533538212', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (23, '2023-04-08 16:48:26.432397', '4', 'username---18533538213', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (24, '2023-04-08 16:48:26.449398', '5', 'username---18533538214', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (25, '2023-04-08 16:48:26.464397', '6', 'username---18533538215', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (26, '2023-04-08 16:48:26.479398', '9', 'username---18533538220', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (27, '2023-04-08 16:48:33.994591', '8', 'username---18533538210', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (28, '2023-04-08 17:24:32.789776', '8', 'username---18533538210', 2, '[{\"changed\": {\"fields\": [\"\\u79ef\\u5206\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (29, '2023-04-15 11:37:07.965155', '5', 'Redis入门课程-第1章-Redis入门课程1', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (30, '2023-04-15 11:37:16.462146', '6', 'Redis入门课程-第1章-Redis入门课程2', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (31, '2023-04-15 11:46:13.140139', '6', 'Redis入门课程-第2章-Redis入门课程2', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u7ae0\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (32, '2023-04-15 11:46:53.943808', '19', 'Redis入门课程-第1章-Redis入门课程1-Redis入门课程', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (33, '2023-04-15 11:49:06.301176', '20', 'Redis入门课程-第1章-Redis入门课程1-Redis入门课程1.2', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (34, '2023-04-15 11:49:11.708601', '21', 'Redis入门课程-第1章-Redis入门课程1-Redis入门课程1.3', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (35, '2023-04-15 11:49:17.771708', '22', 'Redis入门课程-第1章-Redis入门课程1-Redis入门课程1.4', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (36, '2023-04-15 11:49:25.364730', '24', 'Redis入门课程-第2章-Redis入门课程2-Redis入门课程2.2', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (37, '2023-04-15 11:49:29.792463', '25', 'Redis入门课程-第2章-Redis入门课程2-Redis入门课程2.3', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (38, '2023-04-15 11:49:33.988454', '26', 'Redis入门课程-第2章-Redis入门课程2-Redis入门课程2.4', 2, '[{\"changed\": {\"fields\": [\"\\u7b2c\\u51e0\\u8282\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (39, '2023-04-17 21:28:32.189818', '1', 'username---root', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\", \"Last login\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (40, '2023-04-17 21:28:46.400094', '8', 'username---18533538210', 2, '[{\"changed\": {\"fields\": [\"\\u4e2a\\u4eba\\u5934\\u50cf\"]}}]', 9, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (22, 'coupon', 'coupon');
INSERT INTO `django_content_type` VALUES (24, 'coupon', 'couponcourse');
INSERT INTO `django_content_type` VALUES (26, 'coupon', 'couponcoursecat');
INSERT INTO `django_content_type` VALUES (23, 'coupon', 'coupondirection');
INSERT INTO `django_content_type` VALUES (25, 'coupon', 'couponlog');
INSERT INTO `django_content_type` VALUES (16, 'course', 'activity');
INSERT INTO `django_content_type` VALUES (14, 'course', 'course');
INSERT INTO `django_content_type` VALUES (19, 'course', 'courseactivityprice');
INSERT INTO `django_content_type` VALUES (12, 'course', 'coursecategory');
INSERT INTO `django_content_type` VALUES (13, 'course', 'coursechapter');
INSERT INTO `django_content_type` VALUES (15, 'course', 'coursedirection');
INSERT INTO `django_content_type` VALUES (10, 'course', 'courselesson');
INSERT INTO `django_content_type` VALUES (18, 'course', 'discount');
INSERT INTO `django_content_type` VALUES (17, 'course', 'discounttype');
INSERT INTO `django_content_type` VALUES (11, 'course', 'teacher');
INSERT INTO `django_content_type` VALUES (8, 'home', 'banner');
INSERT INTO `django_content_type` VALUES (7, 'home', 'nav');
INSERT INTO `django_content_type` VALUES (20, 'orders', 'order');
INSERT INTO `django_content_type` VALUES (21, 'orders', 'orderdetail');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (27, 'user', 'credit');
INSERT INTO `django_content_type` VALUES (31, 'user', 'studycode');
INSERT INTO `django_content_type` VALUES (30, 'user', 'studynote');
INSERT INTO `django_content_type` VALUES (32, 'user', 'studyprogress');
INSERT INTO `django_content_type` VALUES (29, 'user', 'studyqa');
INSERT INTO `django_content_type` VALUES (28, 'user', 'usercourse');
INSERT INTO `django_content_type` VALUES (9, 'user', 'userinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2023-03-15 02:34:06.473591');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2023-03-15 02:34:10.776977');
INSERT INTO `django_migrations` VALUES (18, 'home', '0001_initial', '2023-03-15 02:34:12.568146');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2023-03-15 02:34:12.747218');
INSERT INTO `django_migrations` VALUES (20, 'home', '0002_banner', '2023-03-15 04:46:51.763790');
INSERT INTO `django_migrations` VALUES (21, 'auth', '0001_initial', '2023-03-16 02:44:24.859577');
INSERT INTO `django_migrations` VALUES (22, 'auth', '0002_alter_permission_name_max_length', '2023-03-16 02:44:25.173568');
INSERT INTO `django_migrations` VALUES (23, 'auth', '0003_alter_user_email_max_length', '2023-03-16 02:44:25.192568');
INSERT INTO `django_migrations` VALUES (24, 'auth', '0004_alter_user_username_opts', '2023-03-16 02:44:25.207568');
INSERT INTO `django_migrations` VALUES (25, 'auth', '0005_alter_user_last_login_null', '2023-03-16 02:44:25.222565');
INSERT INTO `django_migrations` VALUES (26, 'auth', '0006_require_contenttypes_0002', '2023-03-16 02:44:25.236592');
INSERT INTO `django_migrations` VALUES (27, 'auth', '0007_alter_validators_add_error_messages', '2023-03-16 02:44:25.255576');
INSERT INTO `django_migrations` VALUES (28, 'auth', '0008_alter_user_username_max_length', '2023-03-16 02:44:25.268568');
INSERT INTO `django_migrations` VALUES (29, 'auth', '0009_alter_user_last_name_max_length', '2023-03-16 02:44:25.286569');
INSERT INTO `django_migrations` VALUES (30, 'auth', '0010_alter_group_name_max_length', '2023-03-16 02:44:25.315582');
INSERT INTO `django_migrations` VALUES (31, 'auth', '0011_update_proxy_permissions', '2023-03-16 02:44:25.334755');
INSERT INTO `django_migrations` VALUES (32, 'auth', '0012_alter_user_first_name_max_length', '2023-03-16 02:44:25.347756');
INSERT INTO `django_migrations` VALUES (33, 'user', '0001_initial', '2023-03-16 02:44:27.216537');
INSERT INTO `django_migrations` VALUES (34, 'admin', '0001_initial', '2023-03-16 02:44:28.338946');
INSERT INTO `django_migrations` VALUES (35, 'admin', '0002_logentry_remove_auto_add', '2023-03-16 02:44:28.430504');
INSERT INTO `django_migrations` VALUES (36, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-16 02:44:28.475507');
INSERT INTO `django_migrations` VALUES (37, 'user', '0002_userinfo_is_deleted', '2023-03-18 03:19:40.010976');
INSERT INTO `django_migrations` VALUES (38, 'course', '0001_initial', '2023-03-21 15:37:59.198794');
INSERT INTO `django_migrations` VALUES (39, 'course', '0002_auto_20230402_1805', '2023-04-02 18:05:28.592918');
INSERT INTO `django_migrations` VALUES (40, 'user', '0003_alter_userinfo_avatar', '2023-04-02 18:05:28.690933');
INSERT INTO `django_migrations` VALUES (41, 'course', '0003_alter_course_course_type', '2023-04-04 22:09:46.358761');
INSERT INTO `django_migrations` VALUES (42, 'orders', '0001_initial', '2023-04-04 22:09:47.225292');
INSERT INTO `django_migrations` VALUES (43, 'coupon', '0001_initial', '2023-04-06 19:49:11.754497');
INSERT INTO `django_migrations` VALUES (44, 'orders', '0002_auto_20230408_1639', '2023-04-08 16:39:19.158135');
INSERT INTO `django_migrations` VALUES (45, 'user', '0004_credit', '2023-04-08 16:39:19.453134');
INSERT INTO `django_migrations` VALUES (46, 'course', '0004_auto_20230408_1656', '2023-04-08 16:56:29.426995');
INSERT INTO `django_migrations` VALUES (47, 'user', '0005_auto_20230409_1056', '2023-04-09 10:56:53.927481');
INSERT INTO `django_migrations` VALUES (48, 'user', '0006_studycode_studynote_studyprogress_studyqa', '2023-04-15 15:13:50.485472');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for fs_activity
-- ----------------------------
DROP TABLE IF EXISTS `fs_activity`;
CREATE TABLE `fs_activity`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_activity
-- ----------------------------
INSERT INTO `fs_activity` VALUES (1, 1, 0, '2022-02-17 10:42:54.340893', '2022-02-17 10:42:54.340933', 1, '路飞学城-5周年庆', '2022-02-17 00:00:00.000000', '2024-08-01 00:00:00.000000', '<p>5周年庆，各种活动促销内容展示图片</p>', '负责人：\r\n组织：\r\n外勤：');

-- ----------------------------
-- Table structure for fs_banner
-- ----------------------------
DROP TABLE IF EXISTS `fs_banner`;
CREATE TABLE `fs_banner`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `link` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `note` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_http` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_banner
-- ----------------------------
INSERT INTO `fs_banner` VALUES (1, '1', 1, 0, '2022-07-15 03:39:49.859000', '2022-07-15 03:39:51.437000', 1, 'banner/2023/1.jpg', '/project', '暂无', 0);
INSERT INTO `fs_banner` VALUES (2, '2', 1, 0, '2022-07-15 03:39:49.859000', '2022-07-15 03:39:51.437000', 1, 'banner/2023/2.jpg', '/project', '暂无', 0);
INSERT INTO `fs_banner` VALUES (3, '3', 1, 0, '2022-07-15 03:39:49.859000', '2022-07-15 03:39:51.437000', 1, 'banner/2023/3.jpg', '/project', '暂无', 0);
INSERT INTO `fs_banner` VALUES (4, '4', 1, 0, '2022-07-15 03:39:49.859000', '2022-07-15 03:39:51.437000', 1, 'banner/2023/4.jpg', '/project', '暂无', 0);
INSERT INTO `fs_banner` VALUES (5, '5', 1, 0, '2022-07-15 03:39:49.859000', '2022-07-15 03:39:51.437000', 1, 'banner/2023/5.jpg', '/project', '暂无', 0);

-- ----------------------------
-- Table structure for fs_coupon
-- ----------------------------
DROP TABLE IF EXISTS `fs_coupon`;
CREATE TABLE `fs_coupon`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `discount` smallint(6) NOT NULL,
  `coupon_type` smallint(6) NOT NULL,
  `total` int(11) NOT NULL,
  `has_total` int(11) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `get_type` smallint(6) NOT NULL,
  `condition` int(11) NOT NULL,
  `per_limit` smallint(6) NOT NULL,
  `sale` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_coupon
-- ----------------------------
INSERT INTO `fs_coupon` VALUES (1, '30元通用优惠券', 1, 0, '2022-05-04 10:35:40.569417', '2023-06-30 10:25:00.353212', 1, 1, 0, 10000, 10000, '2022-05-04 10:35:00.000000', '2023-11-02 10:35:00.000000', 0, 100, 1, '-30');
INSERT INTO `fs_coupon` VALUES (2, '前端学习通用优惠券', 1, 0, '2022-05-04 10:36:58.401527', '2024-05-04 10:36:58.401556', 1, 1, 1, 100, 100, '2022-05-04 10:36:00.000000', '2024-08-04 10:36:00.000000', 0, 0, 1, '-50');
INSERT INTO `fs_coupon` VALUES (3, 'Typescript课程专用券', 1, 0, '2022-05-04 10:38:36.134581', '2024-05-04 10:38:36.134624', 1, 2, 3, 1000, 1000, '2022-05-04 10:38:00.000000', '2024-08-04 10:38:00.000000', 0, 0, 1, '*0.88');
INSERT INTO `fs_coupon` VALUES (4, 'python七夕专用券', 1, 0, '2022-05-04 10:40:08.022904', '2024-06-30 10:25:46.949197', 1, 1, 2, 200, 200, '2022-05-04 10:39:00.000000', '2024-11-15 10:39:00.000000', 1, 0, 1, '-99');
INSERT INTO `fs_coupon` VALUES (5, '算法学习优惠券', 1, 0, '2021-08-05 10:05:07.837008', '2024-06-30 10:26:12.133812', 1, 2, 2, 1000, 1000, '2022-08-05 10:04:00.000000', '2024-12-25 10:04:00.000000', 0, 200, 1, '*0.85');

-- ----------------------------
-- Table structure for fs_coupon_course
-- ----------------------------
DROP TABLE IF EXISTS `fs_coupon_course`;
CREATE TABLE `fs_coupon_course`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `coupon_id` bigint(20) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_coupon_course_coupon_id_a717cef8`(`coupon_id` ASC) USING BTREE,
  INDEX `fs_coupon_course_course_id_139d689e`(`course_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_coupon_course
-- ----------------------------
INSERT INTO `fs_coupon_course` VALUES (1, '2024-05-04 10:38:36.140929', 3, 1);
INSERT INTO `fs_coupon_course` VALUES (2, '2024-05-04 10:38:36.143166', 3, 2);

-- ----------------------------
-- Table structure for fs_coupon_course_category
-- ----------------------------
DROP TABLE IF EXISTS `fs_coupon_course_category`;
CREATE TABLE `fs_coupon_course_category`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `coupon_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_coupon_course_category_category_id_966fce70`(`category_id` ASC) USING BTREE,
  INDEX `fs_coupon_course_category_coupon_id_0a6eee65`(`coupon_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_coupon_course_category
-- ----------------------------
INSERT INTO `fs_coupon_course_category` VALUES (1, '2023-05-04 10:40:08.029505', 20, 4);
INSERT INTO `fs_coupon_course_category` VALUES (2, '2024-05-04 10:40:08.042891', 21, 4);
INSERT INTO `fs_coupon_course_category` VALUES (3, '2024-08-05 10:05:07.966221', 33, 5);

-- ----------------------------
-- Table structure for fs_coupon_course_direction
-- ----------------------------
DROP TABLE IF EXISTS `fs_coupon_course_direction`;
CREATE TABLE `fs_coupon_course_direction`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `coupon_id` bigint(20) NOT NULL,
  `direction_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_coupon_course_direction_coupon_id_9ca32071`(`coupon_id` ASC) USING BTREE,
  INDEX `fs_coupon_course_direction_direction_id_87b82e2c`(`direction_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_coupon_course_direction
-- ----------------------------
INSERT INTO `fs_coupon_course_direction` VALUES (1, '2024-05-04 10:36:58.414461', 2, 1);

-- ----------------------------
-- Table structure for fs_coupon_log
-- ----------------------------
DROP TABLE IF EXISTS `fs_coupon_log`;
CREATE TABLE `fs_coupon_log`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `use_time` datetime(6) NULL DEFAULT NULL,
  `use_status` smallint(6) NULL DEFAULT NULL,
  `coupon_id` bigint(20) NOT NULL,
  `order_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_coupon_log_coupon_id_924f4534`(`coupon_id` ASC) USING BTREE,
  INDEX `fs_coupon_log_order_id_76acec06`(`order_id` ASC) USING BTREE,
  INDEX `fs_coupon_log_user_id_43b13bdc`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_coupon_log
-- ----------------------------
INSERT INTO `fs_coupon_log` VALUES (5, 1, 0, '2022-05-04 12:00:25.051976', '2023-04-07 12:16:12.443824', 1, '30元通用优惠券222', NULL, 0, 1, NULL, 1);
INSERT INTO `fs_coupon_log` VALUES (8, 1, 0, '2022-05-04 12:03:24.331024', '2023-04-07 12:16:09.601165', 1, '前端学习通用优惠券', NULL, 0, 2, NULL, 1);
INSERT INTO `fs_coupon_log` VALUES (9, 1, 0, '2022-05-04 12:03:31.692397', '2023-04-07 12:16:05.954784', 1, 'Typescript课程专用券', NULL, 0, 3, NULL, 1);
INSERT INTO `fs_coupon_log` VALUES (10, 1, 0, '2022-05-04 12:03:38.225438', '2023-04-07 12:16:03.728060', 1, 'python七夕专用券', NULL, 0, 4, NULL, 1);
INSERT INTO `fs_coupon_log` VALUES (11, 1, 0, '2022-05-04 12:09:25.406437', '2023-04-07 12:15:59.553731', 1, '前端学习通用优惠券', NULL, 0, 2, NULL, 1);
INSERT INTO `fs_coupon_log` VALUES (12, 1, 0, '2021-08-05 10:06:06.036230', '2023-04-07 12:15:50.924882', 1, '算法学习优惠券', NULL, 0, 5, NULL, 1);

-- ----------------------------
-- Table structure for fs_course_activity_price
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_activity_price`;
CREATE TABLE `fs_course_activity_price`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `activity_id` bigint(20) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  `discount_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_course_activity_price_activity_id_4557c07e`(`activity_id` ASC) USING BTREE,
  INDEX `fs_course_activity_price_course_id_54597bc3`(`course_id` ASC) USING BTREE,
  INDEX `fs_course_activity_price_discount_id_4671cb16`(`discount_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_activity_price
-- ----------------------------
INSERT INTO `fs_course_activity_price` VALUES (1, '九折-3天Typescript', 1, 0, '2022-02-17 10:48:12.600755', '2024-02-17 10:48:12.600801', 1, 1, 2, 2);
INSERT INTO `fs_course_activity_price` VALUES (2, '免费送课', 1, 0, '2022-02-17 11:36:34.192896', '2024-02-17 11:36:34.192941', 1, 1, 1, 1);
INSERT INTO `fs_course_activity_price` VALUES (3, '减免课程', 1, 0, '2022-02-17 11:40:49.240245', '2024-02-17 11:40:49.240276', 1, 1, 3, 3);

-- ----------------------------
-- Table structure for fs_course_category
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_category`;
CREATE TABLE `fs_course_category`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `direction_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE,
  INDEX `fs_course_category_direction_id_8b494da4`(`direction_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 70 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_category
-- ----------------------------
INSERT INTO `fs_course_category` VALUES (1, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Vue.js', '', 1);
INSERT INTO `fs_course_category` VALUES (2, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Typescript', '', 1);
INSERT INTO `fs_course_category` VALUES (3, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'React.js', '', 1);
INSERT INTO `fs_course_category` VALUES (4, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'HTML', '', 1);
INSERT INTO `fs_course_category` VALUES (5, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'JavaScript', '', 1);
INSERT INTO `fs_course_category` VALUES (6, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Angular', '', 1);
INSERT INTO `fs_course_category` VALUES (7, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Node.js', '', 1);
INSERT INTO `fs_course_category` VALUES (8, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'WebApp', '', 1);
INSERT INTO `fs_course_category` VALUES (9, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '小程序', '', 1);
INSERT INTO `fs_course_category` VALUES (10, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '前端工具', '', 1);
INSERT INTO `fs_course_category` VALUES (11, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'HTML/CSS', '', 1);
INSERT INTO `fs_course_category` VALUES (12, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Html5', '', 1);
INSERT INTO `fs_course_category` VALUES (13, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'CSS3', '', 1);
INSERT INTO `fs_course_category` VALUES (14, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Java', '', 2);
INSERT INTO `fs_course_category` VALUES (15, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'SpringBoot', '', 2);
INSERT INTO `fs_course_category` VALUES (16, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Spring Cloud', '', 2);
INSERT INTO `fs_course_category` VALUES (17, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'SSM', '', 2);
INSERT INTO `fs_course_category` VALUES (18, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'PHP', '', 2);
INSERT INTO `fs_course_category` VALUES (19, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '.net', '', 2);
INSERT INTO `fs_course_category` VALUES (20, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Python', '', 2);
INSERT INTO `fs_course_category` VALUES (21, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '爬虫', '', 2);
INSERT INTO `fs_course_category` VALUES (22, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Django', '', 2);
INSERT INTO `fs_course_category` VALUES (23, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Flask', '', 2);
INSERT INTO `fs_course_category` VALUES (24, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Go', '', 2);
INSERT INTO `fs_course_category` VALUES (25, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'C', '', 2);
INSERT INTO `fs_course_category` VALUES (26, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'C++', '', 2);
INSERT INTO `fs_course_category` VALUES (27, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'C#', '', 2);
INSERT INTO `fs_course_category` VALUES (28, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Flutter', '', 3);
INSERT INTO `fs_course_category` VALUES (29, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Android', '', 3);
INSERT INTO `fs_course_category` VALUES (30, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'iOS', '', 3);
INSERT INTO `fs_course_category` VALUES (31, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'React native', '', 3);
INSERT INTO `fs_course_category` VALUES (32, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '计算机网络', '', 4);
INSERT INTO `fs_course_category` VALUES (33, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '算法与数据结构', '', 4);
INSERT INTO `fs_course_category` VALUES (34, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '数学', '', 4);
INSERT INTO `fs_course_category` VALUES (35, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '微服务', '', 5);
INSERT INTO `fs_course_category` VALUES (36, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '机器学习', '', 5);
INSERT INTO `fs_course_category` VALUES (37, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '深度学习', '', 5);
INSERT INTO `fs_course_category` VALUES (38, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '计算机视觉', '', 5);
INSERT INTO `fs_course_category` VALUES (39, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '自然语言处理', '', 5);
INSERT INTO `fs_course_category` VALUES (40, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '数据分析&挖掘', '', 5);
INSERT INTO `fs_course_category` VALUES (41, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '大数据', '', 6);
INSERT INTO `fs_course_category` VALUES (42, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Hadoop', '', 6);
INSERT INTO `fs_course_category` VALUES (43, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Spark', '', 6);
INSERT INTO `fs_course_category` VALUES (44, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Hbase', '', 6);
INSERT INTO `fs_course_category` VALUES (45, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Flink', '', 6);
INSERT INTO `fs_course_category` VALUES (46, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Storm', '', 6);
INSERT INTO `fs_course_category` VALUES (47, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '阿里云', '', 7);
INSERT INTO `fs_course_category` VALUES (48, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '容器', '', 7);
INSERT INTO `fs_course_category` VALUES (49, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Docker', '', 7);
INSERT INTO `fs_course_category` VALUES (50, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Kubernetes', '', 7);
INSERT INTO `fs_course_category` VALUES (51, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '运维', '', 8);
INSERT INTO `fs_course_category` VALUES (52, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '自动化运维', '', 8);
INSERT INTO `fs_course_category` VALUES (53, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '中间件', '', 8);
INSERT INTO `fs_course_category` VALUES (54, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Linux', '', 8);
INSERT INTO `fs_course_category` VALUES (55, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '测试', '', 9);
INSERT INTO `fs_course_category` VALUES (56, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '功能测试', '', 9);
INSERT INTO `fs_course_category` VALUES (57, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '性能测试', '', 9);
INSERT INTO `fs_course_category` VALUES (58, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '自动化测试', '', 9);
INSERT INTO `fs_course_category` VALUES (59, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '接口测试', '', 9);
INSERT INTO `fs_course_category` VALUES (60, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'MySQL', '', 10);
INSERT INTO `fs_course_category` VALUES (61, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Redis', '', 10);
INSERT INTO `fs_course_category` VALUES (62, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'MongoDB', '', 10);
INSERT INTO `fs_course_category` VALUES (63, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '设计基础', '', 11);
INSERT INTO `fs_course_category` VALUES (64, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '设计工具', '', 11);
INSERT INTO `fs_course_category` VALUES (65, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'APPUI设计', '', 11);
INSERT INTO `fs_course_category` VALUES (66, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'Unity 3D', '', 13);
INSERT INTO `fs_course_category` VALUES (67, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'cocos creator', '', 13);
INSERT INTO `fs_course_category` VALUES (68, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, '求职面试', '', 14);
INSERT INTO `fs_course_category` VALUES (69, 1, 0, '2021-07-22 08:00:19.366304', '2021-07-22 08:00:19.367343', 1, 'leetcode', '', 14);

-- ----------------------------
-- Table structure for fs_course_chapter
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_chapter`;
CREATE TABLE `fs_course_chapter`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `summary` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `pub_date` date NOT NULL,
  `course_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_course_chapter_course_id_b33e80dc`(`course_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_chapter
-- ----------------------------
INSERT INTO `fs_course_chapter` VALUES (1, 'Typescript快速入门', 1, 0, '2022-03-21 05:39:39.925451', '2022-03-21 05:39:39.925775', 1, '<p>Typescript快速入门的相关概念以及基本安装和基本使用</p>', '2022-03-21', 1);
INSERT INTO `fs_course_chapter` VALUES (2, 'Typescript的基本语法', 1, 0, '2022-03-21 05:40:38.672697', '2022-03-21 05:40:38.672749', 1, '<p>注释、数据类型、类型注解、函数、面向对象语法、泛型等</p>', '2022-03-21', 1);
INSERT INTO `fs_course_chapter` VALUES (5, 'Redis入门课程1', 1, 0, '2023-04-15 11:37:07.960155', '2023-04-15 11:37:07.960155', 1, '<p>Redis入门课程1</p>', '2023-04-15', 20);
INSERT INTO `fs_course_chapter` VALUES (6, 'Redis入门课程2', 1, 0, '2023-04-15 11:37:16.461144', '2023-04-15 11:46:13.132138', 2, '<p>Redis入门课程2</p>', '2023-04-15', 20);

-- ----------------------------
-- Table structure for fs_course_direction
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_direction`;
CREATE TABLE `fs_course_direction`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `recomment_home_hot` tinyint(1) NOT NULL,
  `recomment_home_top` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_direction
-- ----------------------------
INSERT INTO `fs_course_direction` VALUES (1, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '前端开发', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (2, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '后端开发', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (3, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '移动开发', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (4, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '计算机基础', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (5, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '前沿技术', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (6, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '云计算', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (7, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '大数据', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (8, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '运维', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (9, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '测试', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (10, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '数据库', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (11, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, 'UI设计', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (12, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '多媒体', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (13, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '游戏', '', 1, 1);
INSERT INTO `fs_course_direction` VALUES (14, 1, 0, '2021-07-22 05:42:01.290060', '2021-07-22 05:42:01.290088', 1, '求职面试', '', 1, 1);

-- ----------------------------
-- Table structure for fs_course_info
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_info`;
CREATE TABLE `fs_course_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `course_cover` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `course_video` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `course_type` smallint(6) NOT NULL,
  `level` smallint(6) NOT NULL,
  `status` smallint(6) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `pub_date` date NOT NULL,
  `period` int(11) NOT NULL,
  `attachment_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `attachment_link` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `students` int(11) NOT NULL,
  `lessons` int(11) NOT NULL,
  `pub_lessons` int(11) NOT NULL,
  `price` decimal(10, 2) NULL DEFAULT NULL,
  `recomment_home_hot` tinyint(1) NOT NULL,
  `recomment_home_top` tinyint(1) NOT NULL,
  `category_id` bigint(20) NULL DEFAULT NULL,
  `direction_id` bigint(20) NULL DEFAULT NULL,
  `teacher_id` bigint(20) NULL DEFAULT NULL,
  `credit` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_course_info_category_id_0e52ca0f`(`category_id` ASC) USING BTREE,
  INDEX `fs_course_info_direction_id_2a2791a9`(`direction_id` ASC) USING BTREE,
  INDEX `fs_course_info_teacher_id_b137ee12`(`teacher_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_info
-- ----------------------------
INSERT INTO `fs_course_info` VALUES (1, '7天Typescript从入门到放弃', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-10.png', '', 0, 0, 0, '<p>7天Typescript从入门到放弃</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 1100, 70, 15, 800.00, 0, 0, 2, 1, 1, 0);
INSERT INTO `fs_course_info` VALUES (2, '3天Typescript精修', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-9.png', '', 0, 0, 0, '<p>3天Typescript精修</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 9704, 100, 100, 998.00, 1, 0, 2, 1, 2, 0);
INSERT INTO `fs_course_info` VALUES (3, '3天学会Vue基础', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-8.png', '', 0, 0, 0, '<p>3天学会Vue基础</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 988, 130, 54, 500.00, 1, 0, 1, 1, 2, 0);
INSERT INTO `fs_course_info` VALUES (4, '算法与数据结构体系课', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-7.png', '', 0, 0, 0, '<p>算法与数据结构体系课</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 1303, 150, 50, 998.00, 0, 1, 33, 4, 4, 0);
INSERT INTO `fs_course_info` VALUES (5, 'python基础入门', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-6.png', '', 0, 0, 0, '<p>python基础入门</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 4302, 140, 30, 100.00, 0, 1, 20, 2, 4, 0);
INSERT INTO `fs_course_info` VALUES (6, 'javascript进阶', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-5.png', '', 0, 0, 0, '<p>javascript进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 1125, 180, 100, 1750.00, 1, 0, 5, 1, 3, 0);
INSERT INTO `fs_course_info` VALUES (7, '爬虫进阶之逆向工程', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-4.png', '', 0, 0, 0, '<p>爬虫进阶之逆向工程</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 223, 145, 55, 400.00, 0, 0, 21, 2, 3, 0);
INSERT INTO `fs_course_info` VALUES (8, 'Kubernetes 入门到进阶实战', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-3.png', '', 0, 0, 0, '<p>Kubernetes 入门到进阶实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 6074, 70, 20, 500.00, 1, 0, 50, 7, 3, 0);
INSERT INTO `fs_course_info` VALUES (9, 'Android 应用程序构建实战', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-2.png', '', 0, 0, 0, '<p>Android 应用程序构建实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 1059, 110, 50, 550.00, 0, 0, 29, 3, 1, 0);
INSERT INTO `fs_course_info` VALUES (10, 'Kotlin从入门到精通', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-1.png', '', 0, 0, 0, '<p>Kotlin从入门到精通</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 870, 120, 0, 500.00, 1, 0, 29, 3, 1, 0);
INSERT INTO `fs_course_info` VALUES (11, '深度学习之神经网络', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-11.png', '', 0, 0, 0, '<p>深度学习之神经网络</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 6002, 115, 70, 80.00, 1, 0, 37, 5, 1, 0);
INSERT INTO `fs_course_info` VALUES (12, 'OpenCV入门到进阶', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-12.png', '', 0, 0, 0, '<p>OpenCV入门到进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 1029, 100, 70, 390.00, 0, 1, 38, 5, 2, 0);
INSERT INTO `fs_course_info` VALUES (13, 'Go容器化微服务系统实战', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-13.png', '', 0, 0, 0, '<p>Go容器化微服务系统实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 24202, 65, 65, 399.00, 0, 0, 35, 5, 1, 0);
INSERT INTO `fs_course_info` VALUES (14, 'RabbitMQ精讲', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-14.png', '', 0, 0, 0, '<p>RabbitMQ精讲</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 980, 100, 100, 710.00, 0, 0, 53, 8, 4, 0);
INSERT INTO `fs_course_info` VALUES (15, 'TensorFlow基础', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-15.png', '', 0, 0, 0, '<p>RabbitMQ精讲</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 670, 220, 100, 1590.00, 0, 1, 36, 5, 2, 0);
INSERT INTO `fs_course_info` VALUES (16, 'ZooKeeper分布式架构搭建', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-16.png', '', 0, 0, 0, '<p>ZooKeeper分布式架构搭建</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 90, 88, 35, 40.00, 1, 0, 35, 5, 3, 0);
INSERT INTO `fs_course_info` VALUES (17, '高性能MySQL调优', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-17.png', '', 0, 0, 0, '<p>高性能MySQL调优</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 40, 300, 60, 998.00, 1, 1, 60, 10, 3, 0);
INSERT INTO `fs_course_info` VALUES (18, 'MySQL事务处理精选', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-18.png', '', 0, 0, 0, '<p>MySQL事务处理精选</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 640, 65, 30, 1000.00, 1, 0, 60, 10, 1, 0);
INSERT INTO `fs_course_info` VALUES (19, 'MongoDB入门到进阶', 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 1, 'course/cover/course-19.png', '', 0, 0, 0, '<p>MongoDB入门到进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 11205, 86, 40, 1100.00, 0, 1, 62, 10, 3, 0);
INSERT INTO `fs_course_info` VALUES (20, 'Redis入门课程', 1, 0, '2021-07-22 04:35:05.696823', '2023-04-02 13:34:56.544375', 1, 'course/cover/course-20.png', 'course/video/1_CdR4TRL.mp4', 0, 0, 0, '<p>Redis入门课程</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', NULL, 166, 100, 40, 1199.00, 1, 1, 61, 10, 2, 10);

-- ----------------------------
-- Table structure for fs_course_lesson
-- ----------------------------
DROP TABLE IF EXISTS `fs_course_lesson`;
CREATE TABLE `fs_course_lesson`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `lesson_type` smallint(6) NOT NULL,
  `lesson_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `duration` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pub_date` datetime(6) NOT NULL,
  `free_trail` tinyint(1) NOT NULL,
  `recomment` tinyint(1) NOT NULL,
  `chapter_id` bigint(20) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_course_lesson_chapter_id_5461296b`(`chapter_id` ASC) USING BTREE,
  INDEX `fs_course_lesson_course_id_088e9a8a`(`course_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_course_lesson
-- ----------------------------
INSERT INTO `fs_course_lesson` VALUES (1, 'Typescript基本介绍', 1, 0, '2022-03-21 05:41:47.975350', '2022-03-21 05:41:47.975495', 1, 2, '085a2e302a675951ad88c4480a8920df_0', '5:00', '2022-03-21 05:41:47.975554', 1, 1, 1, 1);
INSERT INTO `fs_course_lesson` VALUES (2, 'Typescript与javascript的关系', 1, 0, '2022-03-21 05:42:13.059002', '2022-03-21 05:42:13.059077', 2, 2, '085a2e302a675951ad88c4480a8920df_0', '3:00', '2022-03-21 05:42:13.059128', 1, 1, 1, 1);
INSERT INTO `fs_course_lesson` VALUES (3, 'Typescript基本安装', 1, 0, '2022-03-21 05:42:29.797695', '2022-03-21 05:42:29.797750', 3, 2, '085a2e302a675951ad88c4480a8920df_0', '10:00', '2022-03-21 05:42:29.797796', 1, 1, 1, 1);
INSERT INTO `fs_course_lesson` VALUES (4, 'Typescript快速使用', 1, 0, '2022-03-21 05:42:43.776543', '2022-03-21 05:42:43.776618', 4, 2, '085a2e302a675951ad88c4480a8920df_0', '10:00', '2022-03-21 05:42:43.776672', 1, 1, 1, 1);
INSERT INTO `fs_course_lesson` VALUES (5, 'Typescript的解释器基本使用', 1, 0, '2022-03-21 05:43:07.315028', '2022-03-21 05:43:07.315092', 5, 2, '085a2e302a675951ad88c4480a8920df_0', '10:00', '2022-03-21 05:43:07.315150', 1, 1, 1, 1);
INSERT INTO `fs_course_lesson` VALUES (6, 'Typescript的注释写法', 1, 0, '2022-03-21 05:43:43.696556', '2022-03-21 05:43:43.696611', 1, 2, '085a2e302a675951ad88c4480a8920df_0', '4:00', '2022-03-21 05:43:43.696656', 1, 0, 2, 1);
INSERT INTO `fs_course_lesson` VALUES (7, 'Typescript的变量声明', 1, 0, '2022-03-21 05:44:06.271049', '2022-03-21 05:44:06.271109', 2, 2, '085a2e302a675951ad88c4480a8920df_0', '4:00', '2022-03-21 05:44:06.271160', 0, 0, 2, 1);
INSERT INTO `fs_course_lesson` VALUES (8, 'Typescript的类型注解', 1, 0, '2022-03-21 05:44:17.103618', '2022-03-21 05:44:17.103717', 3, 2, '085a2e302a675951ad88c4480a8920df_0', '4:00', '2022-03-21 05:44:17.103765', 0, 0, 2, 1);
INSERT INTO `fs_course_lesson` VALUES (19, 'Redis入门课程1.1', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:46:53.935911', 1, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 5, 20);
INSERT INTO `fs_course_lesson` VALUES (20, 'Redis入门课程1.2', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:06.293876', 2, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 5, 20);
INSERT INTO `fs_course_lesson` VALUES (21, 'Redis入门课程1.3', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:11.699601', 3, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 5, 20);
INSERT INTO `fs_course_lesson` VALUES (22, 'Redis入门课程1.4', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:17.762599', 4, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 5, 20);
INSERT INTO `fs_course_lesson` VALUES (23, 'Redis入门课程2.1', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:46:53.935911', 1, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 6, 20);
INSERT INTO `fs_course_lesson` VALUES (24, 'Redis入门课程2.2', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:25.357730', 2, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 6, 20);
INSERT INTO `fs_course_lesson` VALUES (25, 'Redis入门课程2.3', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:29.783465', 3, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 6, 20);
INSERT INTO `fs_course_lesson` VALUES (26, 'Redis入门课程2.4', 1, 0, '2023-04-15 11:46:53.935911', '2023-04-15 11:49:33.980453', 4, 2, '085a2e302a675951ad88c4480a8920df_0', '00:25', '2023-04-15 11:46:53.935911', 0, 0, 6, 20);

-- ----------------------------
-- Table structure for fs_credit
-- ----------------------------
DROP TABLE IF EXISTS `fs_credit`;
CREATE TABLE `fs_credit`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `operation` smallint(6) NOT NULL,
  `number` int(11) NOT NULL,
  `remark` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_credit_user_id_f078f6db`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_credit
-- ----------------------------
INSERT INTO `fs_credit` VALUES (1, '', 1, 0, '2023-04-08 16:45:59.361293', '2023-04-08 16:45:59.361293', 0, 2, 5, NULL, 1);
INSERT INTO `fs_credit` VALUES (2, '', 1, 0, '2023-04-08 16:46:11.780753', '2023-04-08 16:46:11.780753', 0, 2, 95, NULL, 1);
INSERT INTO `fs_credit` VALUES (4, '', 1, 0, '2023-04-08 16:48:33.911826', '2023-04-08 16:48:33.911826', 0, 2, 0, NULL, 8);
INSERT INTO `fs_credit` VALUES (5, '', 1, 0, '2023-04-08 17:24:32.656778', '2023-04-08 17:24:32.656778', 0, 2, 50, NULL, 8);
INSERT INTO `fs_credit` VALUES (6, '', 1, 0, '2023-04-17 21:28:31.988210', '2023-04-17 21:28:31.988210', 0, 2, 0, NULL, 1);
INSERT INTO `fs_credit` VALUES (7, '', 1, 0, '2023-04-17 21:28:46.313093', '2023-04-17 21:28:46.313093', 0, 2, 0, NULL, 8);

-- ----------------------------
-- Table structure for fs_discount
-- ----------------------------
DROP TABLE IF EXISTS `fs_discount`;
CREATE TABLE `fs_discount`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `condition` int(11) NOT NULL,
  `sale` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `discount_type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_discount_discount_type_id_4e8e4202`(`discount_type_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_discount
-- ----------------------------
INSERT INTO `fs_discount` VALUES (1, '免费购买', 1, 0, '2022-02-17 10:45:54.027034', '2024-02-17 10:45:54.027079', 1, 0, '0', 4);
INSERT INTO `fs_discount` VALUES (2, '九折折扣', 1, 0, '2022-02-17 10:47:12.855454', '2024-02-17 11:32:27.148655', 1, 1, '*0.9', 2);
INSERT INTO `fs_discount` VALUES (3, '课程减免100', 1, 0, '2022-02-17 11:40:44.499026', '2024-02-17 11:40:44.499060', 1, 300, '-100', 3);

-- ----------------------------
-- Table structure for fs_discount_type
-- ----------------------------
DROP TABLE IF EXISTS `fs_discount_type`;
CREATE TABLE `fs_discount_type`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_discount_type
-- ----------------------------
INSERT INTO `fs_discount_type` VALUES (1, '免费', 1, 0, '2022-02-17 10:43:38.546870', '2024-02-17 10:43:38.546901', 1, NULL);
INSERT INTO `fs_discount_type` VALUES (2, '折扣', 1, 0, '2022-02-17 10:43:49.161997', '2024-02-17 11:19:58.799363', 1, NULL);
INSERT INTO `fs_discount_type` VALUES (3, '减免', 1, 0, '2022-02-17 10:44:05.712935', '2024-02-17 11:41:16.504340', 1, NULL);
INSERT INTO `fs_discount_type` VALUES (4, '限时免费', 1, 0, '2022-02-17 10:44:23.053845', '2024-02-17 10:44:23.053925', 1, NULL);
INSERT INTO `fs_discount_type` VALUES (5, '限时折扣', 1, 0, '2022-02-17 10:44:31.999352', '2024-02-17 10:44:31.999382', 1, NULL);
INSERT INTO `fs_discount_type` VALUES (6, '限时减免', 1, 0, '2022-02-17 10:44:39.100270', '2024-02-17 10:44:39.100305', 1, NULL);

-- ----------------------------
-- Table structure for fs_nav
-- ----------------------------
DROP TABLE IF EXISTS `fs_nav`;
CREATE TABLE `fs_nav`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_http` tinyint(1) NOT NULL,
  `position` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_nav
-- ----------------------------
INSERT INTO `fs_nav` VALUES (1, '测试项目', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 0);
INSERT INTO `fs_nav` VALUES (2, '测试项目', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 0);
INSERT INTO `fs_nav` VALUES (3, '测试项目', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 0);
INSERT INTO `fs_nav` VALUES (4, '测试项目', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 0);
INSERT INTO `fs_nav` VALUES (5, '路飞外链', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, 'https://www.luffycity.com', 1, 0);
INSERT INTO `fs_nav` VALUES (6, '企业服务', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (7, '关于我们', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (8, '联系我们', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (9, '商务合作', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (10, '帮助中心', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (11, '意见反馈', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);
INSERT INTO `fs_nav` VALUES (12, '新手指南', 1, 0, '2021-07-15 01:27:27.350000', '2021-07-15 01:27:28.690000', 1, '/project', 0, 1);

-- ----------------------------
-- Table structure for fs_order
-- ----------------------------
DROP TABLE IF EXISTS `fs_order`;
CREATE TABLE `fs_order`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `total_price` decimal(10, 2) NOT NULL,
  `real_price` decimal(10, 2) NOT NULL,
  `order_number` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `order_status` smallint(6) NOT NULL,
  `pay_type` smallint(6) NOT NULL,
  `order_desc` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `pay_time` datetime(6) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `credit` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_order_user_id_356a97a4`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_order
-- ----------------------------
INSERT INTO `fs_order` VALUES (1, '购买课程', 1, 0, '2023-04-11 22:14:43.952231', '2023-04-11 22:15:28.329951', 0, 2339.00, 2339.00, '202304110000000100000001', 1, 0, NULL, '2023-04-11 22:15:28.329951', 1, 0);
INSERT INTO `fs_order` VALUES (2, '购买课程', 1, 0, '2023-04-11 22:20:08.362098', '2023-04-11 22:20:08.373097', 0, 1000.00, 1000.00, '202304110000000100000002', 0, 0, NULL, NULL, 1, 0);

-- ----------------------------
-- Table structure for fs_order_course
-- ----------------------------
DROP TABLE IF EXISTS `fs_order_course`;
CREATE TABLE `fs_order_course`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `real_price` decimal(10, 2) NOT NULL,
  `discount_name` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_order_course_course_id_c4e66951`(`course_id` ASC) USING BTREE,
  INDEX `fs_order_course_order_id_2e9d0629`(`order_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_order_course
-- ----------------------------
INSERT INTO `fs_order_course` VALUES (1, 'ZooKeeper分布式架构搭建', 1, 0, '2023-04-11 22:14:43.988233', '2023-04-11 22:14:43.988233', 0, 40.00, 40.00, '', 16, 1);
INSERT INTO `fs_order_course` VALUES (2, 'MongoDB入门到进阶', 1, 0, '2023-04-11 22:14:43.988233', '2023-04-11 22:14:43.988233', 0, 1100.00, 1100.00, '', 19, 1);
INSERT INTO `fs_order_course` VALUES (3, 'Redis入门课程', 1, 0, '2023-04-11 22:14:43.988233', '2023-04-11 22:14:43.988233', 0, 1199.00, 1199.00, '', 20, 1);
INSERT INTO `fs_order_course` VALUES (4, 'MySQL事务处理精选', 1, 0, '2023-04-11 22:20:08.372097', '2023-04-11 22:20:08.372097', 0, 1000.00, 1000.00, '', 18, 2);

-- ----------------------------
-- Table structure for fs_study_code
-- ----------------------------
DROP TABLE IF EXISTS `fs_study_code`;
CREATE TABLE `fs_study_code`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `chapter_id` bigint(20) NULL DEFAULT NULL,
  `course_id` bigint(20) NOT NULL,
  `lesson_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_study_code_chapter_id_4fec22d9`(`chapter_id` ASC) USING BTREE,
  INDEX `fs_study_code_course_id_f7e98260`(`course_id` ASC) USING BTREE,
  INDEX `fs_study_code_lesson_id_d02b7c13`(`lesson_id` ASC) USING BTREE,
  INDEX `fs_study_code_user_id_612025eb`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_study_code
-- ----------------------------

-- ----------------------------
-- Table structure for fs_study_note
-- ----------------------------
DROP TABLE IF EXISTS `fs_study_note`;
CREATE TABLE `fs_study_note`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `chapter_id` bigint(20) NULL DEFAULT NULL,
  `course_id` bigint(20) NOT NULL,
  `lesson_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_study_note_chapter_id_f26abe28`(`chapter_id` ASC) USING BTREE,
  INDEX `fs_study_note_course_id_afa5cabe`(`course_id` ASC) USING BTREE,
  INDEX `fs_study_note_lesson_id_97df1fff`(`lesson_id` ASC) USING BTREE,
  INDEX `fs_study_note_user_id_14e68704`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_study_note
-- ----------------------------

-- ----------------------------
-- Table structure for fs_study_progress
-- ----------------------------
DROP TABLE IF EXISTS `fs_study_progress`;
CREATE TABLE `fs_study_progress`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `study_time` int(11) NOT NULL,
  `lesson_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_study_progress_lesson_id_659287b1`(`lesson_id` ASC) USING BTREE,
  INDEX `fs_study_progress_user_id_95d31409`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_study_progress
-- ----------------------------
INSERT INTO `fs_study_progress` VALUES (1, 25, 19, 1);
INSERT INTO `fs_study_progress` VALUES (2, 20, 20, 1);
INSERT INTO `fs_study_progress` VALUES (3, 20, 21, 1);
INSERT INTO `fs_study_progress` VALUES (4, 15, 23, 1);
INSERT INTO `fs_study_progress` VALUES (5, 0, 24, 1);
INSERT INTO `fs_study_progress` VALUES (6, 10, 25, 1);

-- ----------------------------
-- Table structure for fs_study_qa
-- ----------------------------
DROP TABLE IF EXISTS `fs_study_qa`;
CREATE TABLE `fs_study_qa`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `answer` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `chapter_id` bigint(20) NULL DEFAULT NULL,
  `course_id` bigint(20) NOT NULL,
  `lesson_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_study_qa_chapter_id_f891efab`(`chapter_id` ASC) USING BTREE,
  INDEX `fs_study_qa_course_id_d1959538`(`course_id` ASC) USING BTREE,
  INDEX `fs_study_qa_lesson_id_32287030`(`lesson_id` ASC) USING BTREE,
  INDEX `fs_study_qa_user_id_bcece699`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_study_qa
-- ----------------------------

-- ----------------------------
-- Table structure for fs_teacher
-- ----------------------------
DROP TABLE IF EXISTS `fs_teacher`;
CREATE TABLE `fs_teacher`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `role` smallint(6) NOT NULL,
  `title` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `signature` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `brief` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_teacher
-- ----------------------------
INSERT INTO `fs_teacher` VALUES (1, '张老师', 1, 0, '2021-07-22 04:31:27.741562', '2021-07-22 04:31:27.741708', 1, 0, 'BAT中某某技术总监', 'xxxxxxxx', 'teacher/avatar.jpg', '<p>2009入行，在IT行业深耕13年，删库无数，行内同行送称号：删库小王子。</p>');
INSERT INTO `fs_teacher` VALUES (2, '李老师', 1, 0, '2021-07-22 04:31:27.741562', '2021-07-22 04:31:27.741708', 1, 0, 'BAT中某某技术顾问', 'xxxxxxxx', 'teacher/avatar.jpg', '<p>百变小王子，各种框架信手拈来。</p>');
INSERT INTO `fs_teacher` VALUES (3, '王老师', 1, 0, '2021-07-22 04:31:27.741562', '2021-07-22 04:31:27.741708', 1, 0, 'BAT中某某技术主管', 'xxxxxxxx', 'teacher/avatar.jpg', '<p>草根站长，专注运维20年。</p>');
INSERT INTO `fs_teacher` VALUES (4, '红老师', 1, 0, '2021-07-22 04:31:27.741562', '2023-03-22 15:54:57.032315', 1, 0, 'BAT中某某项目经理', 'xxxxxxxx', 'teacher/avatar.jpg', '<p>美女讲师，说话好听。</p>');
INSERT INTO `fs_teacher` VALUES (6, '赵小明', 1, 0, '2023-03-22 16:00:20.071335', '2023-03-22 16:00:20.071335', 0, 1, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数');
INSERT INTO `fs_teacher` VALUES (7, '梁敏', 1, 0, '2023-03-22 16:02:49.517691', '2023-03-22 16:02:49.517691', 0, 1, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：18510872892，邮箱地址：juan51@yangchen.cn');
INSERT INTO `fs_teacher` VALUES (8, '杨秀芳', 1, 0, '2023-03-22 16:02:49.612692', '2023-03-22 16:02:49.612692', 0, 0, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：15524590974，邮箱地址：yang73@tanxie.cn');
INSERT INTO `fs_teacher` VALUES (9, '李建', 1, 0, '2023-03-22 16:02:49.625691', '2023-03-22 16:02:49.625691', 0, 1, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：13327942719，邮箱地址：qiang69@junjiang.cn');
INSERT INTO `fs_teacher` VALUES (10, '徐雷', 1, 0, '2023-03-22 16:02:49.641717', '2023-03-22 16:02:49.641717', 0, 0, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：15994531716，邮箱地址：minxia@guiying.cn');
INSERT INTO `fs_teacher` VALUES (11, '张玉华', 1, 0, '2023-03-22 16:02:49.656696', '2023-03-22 16:02:49.656696', 0, 0, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：18622932973，邮箱地址：txia@dailuo.cn');
INSERT INTO `fs_teacher` VALUES (12, '师成', 1, 0, '2023-03-22 16:02:49.672691', '2023-03-22 16:02:49.672691', 0, 2, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：15649573941，邮箱地址：klai@liyan.cn');
INSERT INTO `fs_teacher` VALUES (13, '宗璐', 1, 0, '2023-03-22 16:02:49.686693', '2023-03-22 16:02:49.686693', 0, 1, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：13773224956，邮箱地址：tao09@pinglong.cn');
INSERT INTO `fs_teacher` VALUES (14, '张建平', 1, 0, '2023-03-22 16:02:49.702307', '2023-03-22 16:02:49.702307', 0, 2, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：18196313207，邮箱地址：zhengyang@wei.cn');
INSERT INTO `fs_teacher` VALUES (15, '罗坤', 1, 0, '2023-03-22 16:02:49.717983', '2023-03-22 16:02:49.717983', 0, 0, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：18696930767，邮箱地址：changlei@07.cn');
INSERT INTO `fs_teacher` VALUES (16, '涂莹', 1, 0, '2023-03-22 16:02:49.732982', '2023-03-22 16:02:49.732982', 0, 0, '老师', '从业3年，管理班级无数', 'teacher/avatar.jpg', '从业3年，管理班级无数，联系电话：14593810887，邮箱地址：ming46@chaoye.cn');

-- ----------------------------
-- Table structure for fs_user
-- ----------------------------
DROP TABLE IF EXISTS `fs_user`;
CREATE TABLE `fs_user`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `money` decimal(9, 2) NOT NULL,
  `credit` int(11) NOT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `nickname` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `study_time` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE,
  UNIQUE INDEX `mobile`(`mobile` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_user
-- ----------------------------
INSERT INTO `fs_user` VALUES (1, 'pbkdf2_sha256$260000$iCPFW0OaTPBFJfmqKDEQ5Q$SN7BsBXaxBXQyphVQw7jrc/Ei0ul1EVhRwkm4XhdGW4=', '2023-04-15 11:36:00.000000', 1, 'root', '', '', 'hankewei0224@163.com', 1, 1, '2023-03-16 02:44:00.000000', '', 0.00, 1000, 'avatar/2023/avatar.jpeg', 'hankewei', 0, 0);
INSERT INTO `fs_user` VALUES (8, 'pbkdf2_sha256$260000$mWTwjw6C0dln8weAuRQnfV$dixTm4CgExIwrAjd3DJmMQEdtwfwivDy05gZIT+ibS0=', NULL, 0, '18533538210', '', '', '', 0, 1, '2023-03-18 06:38:00.000000', '18533538210', 0.00, 50, 'avatar/2023/avatar_cm9EluL.jpeg', '', 0, 0);

-- ----------------------------
-- Table structure for fs_user_course
-- ----------------------------
DROP TABLE IF EXISTS `fs_user_course`;
CREATE TABLE `fs_user_course`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint(6) NOT NULL,
  `study_time` int(11) NOT NULL,
  `chapter_id` bigint(20) NULL DEFAULT NULL,
  `course_id` bigint(20) NOT NULL,
  `lesson_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fs_user_course_chapter_id_60ab33bc`(`chapter_id` ASC) USING BTREE,
  INDEX `fs_user_course_course_id_a3b1ec2a`(`course_id` ASC) USING BTREE,
  INDEX `fs_user_course_lesson_id_977a9110`(`lesson_id` ASC) USING BTREE,
  INDEX `fs_user_course_user_id_41d16857`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_user_course
-- ----------------------------
INSERT INTO `fs_user_course` VALUES (1, '', 1, 0, '2023-04-11 22:15:28.337954', '2023-04-11 22:15:28.337954', 0, 0, NULL, 16, NULL, 1);
INSERT INTO `fs_user_course` VALUES (2, '', 1, 0, '2023-04-11 22:15:28.337954', '2023-04-11 22:15:28.337954', 0, 0, NULL, 19, NULL, 1);
INSERT INTO `fs_user_course` VALUES (3, '', 1, 0, '2023-04-11 22:15:28.337954', '2023-04-15 15:54:59.805960', 0, 90, 6, 20, 21, 1);

-- ----------------------------
-- Table structure for fs_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `fs_user_groups`;
CREATE TABLE `fs_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userinfo_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `fs_user_groups_userinfo_id_group_id_a35711dd_uniq`(`userinfo_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `fs_user_groups_group_id_988c9c7c_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `fs_user_groups_group_id_988c9c7c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fs_user_groups_userinfo_id_0d0c9b45_fk_fs_user_id` FOREIGN KEY (`userinfo_id`) REFERENCES `fs_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for fs_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `fs_user_user_permissions`;
CREATE TABLE `fs_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userinfo_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `fs_user_user_permissions_userinfo_id_permission_id_d0d32a5a_uniq`(`userinfo_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `fs_user_user_permiss_permission_id_5d1775bc_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `fs_user_user_permiss_permission_id_5d1775bc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fs_user_user_permissions_userinfo_id_feb34eba_fk_fs_user_id` FOREIGN KEY (`userinfo_id`) REFERENCES `fs_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fs_user_user_permissions
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
