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

 Date: 11/11/2020 17:22:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bugfk_market
-- ----------------------------
DROP TABLE IF EXISTS `bugfk_market`;
CREATE TABLE `bugfk_market`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `market_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '市场名称',
  `flag` int(255) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
