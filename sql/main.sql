/*user table for login/up*/
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  userid int AUTO_INCREMENT,
  `user` varchar(30) DEFAULT NULL,
  pswd varchar(32) DEFAULT NULL,
  primary key(userid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;
INSERT INTO `user` VALUES (,'mc','e10adc3949ba59abbe56e057f20f883e');
UNLOCK TABLES;

/*u*/