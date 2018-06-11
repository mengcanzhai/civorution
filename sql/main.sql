DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user` varchar(30) DEFAULT NULL,
  `pswd` varchar(32) DEFAULT NULL,
  `userid` 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;
INSERT INTO `user` VALUES ('mc','e10adc3949ba59abbe56e057f20f883e');
UNLOCK TABLES;
