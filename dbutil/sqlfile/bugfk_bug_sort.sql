/*
 Navicat Premium Data Transfer

 Source Server         : a123456789
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : cdb-q35wa9cy.cd.tencentcdb.com:10094
 Source Schema         : xpw_bugpro

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 11/11/2020 17:22:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bugfk_bug_sort
-- ----------------------------
DROP TABLE IF EXISTS `bugfk_bug_sort`;
CREATE TABLE `bugfk_bug_sort`  (
  `sort_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `sort_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分类名称',
  `sort_type` int(255) NULL DEFAULT NULL COMMENT '分类类型\r\n0.pc端 1.安卓端 2.ios端',
  `flag` int(255) NOT NULL DEFAULT 0 COMMENT '标记 0显示 1不显示',
  PRIMARY KEY (`sort_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
