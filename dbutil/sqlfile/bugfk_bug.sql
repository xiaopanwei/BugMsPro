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

 Date: 11/11/2020 17:22:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bugfk_bug
-- ----------------------------
DROP TABLE IF EXISTS `bugfk_bug`;
CREATE TABLE `bugfk_bug`  (
  `bug_id` int(255) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `client_type` int(255) NULL DEFAULT NULL COMMENT '客户端类型\r\n0.pc端 1.安卓端 2.ios端',
  `belong_project` int(255) NULL DEFAULT NULL COMMENT '所属产品(关联产品表)',
  `belong_bug_sort` int(255) NULL DEFAULT NULL COMMENT '所属BUG分类（关联bug分类表',
  `bug_title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'bug标题',
  `bug_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'bug详情',
  `solve_state` int(255) NULL DEFAULT NULL COMMENT '处理状态\r\n0.未处理 1.处理中 2.已驳回 3.处理完成 4.暂时搁置',
  `solve_method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理办法',
  `submit_person` int(255) NULL DEFAULT NULL COMMENT '反馈人id（关联用户表）',
  `solve_person` int(255) NULL DEFAULT NULL COMMENT '处理人id（关联用户表）',
  `submit_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '反馈时间',
  `solve_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理时间（更新状态时更新时间',
  `reject_reason` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '驳回原因',
  `version` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '程序版本号',
  `flag` int(255) NOT NULL DEFAULT 0 COMMENT '标记 0显示 1不显示',
  `market` int(255) NULL DEFAULT NULL COMMENT '市场（关联市场表）',
  PRIMARY KEY (`bug_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
