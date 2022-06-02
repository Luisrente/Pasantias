

CREATE TABLE `Pasas1`.`Course_viewed` ( `id` BIGINT NOT NULL AUTO_INCREMENT , `idevent` BIGINT(10) NOT NULL , `eventname` VARCHAR(100) NOT NULL , `component` VARCHAR(100) NOT NULL , `action` VARCHAR(100) NOT NULL , `crud` VARCHAR(1) NOT NULL , `userid` BIGINT(10) NOT NULL , `courseid` BIGINT(10) NOT NULL , `Date` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

INSERT INTO `Course_viewed` (`id`, `idevent`, `eventname`, `component`, `action`, `crud`, `userid`, `courseid`, `Date`) VALUES (NULL, '', '', '', '', '', '', '', '')


SELECT 
mdl_logstore_standard_log.id,eventname,component,action,
crud,userid,courseid,
from_unixtime(mdl_logstore_standard_log.timecreated,'%Y') AS ANNO,
from_unixtime(mdl_logstore_standard_log.timecreated,'%b') AS MES,
from_unixtime(mdl_logstore_standard_log.timecreated,'%d') AS DIA,
DATE_FORMAT(FROM_UNIXTIME(mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS "Restored",
(mdl_logstore_standard_log.courseid) AS IdCourse,
mdl_course.id,
mdl_course.fullname ,
(mdl_course_categories.name) AS NombrePrograma,
(mdl_course_categories.id) AS Idprograma,
(mdl_course_categories.parent) AS Idfacultad,
facultad.name
FROM mdl_logstore_standard_log  
INNER JOIN mdl_course ON  mdl_logstore_standard_log.courseid= mdl_course.id   
INNER JOIN mdl_course_categories ON  mdl_course.category= mdl_course_categories.id
INNER JOIN mdl_course_categories AS facultad ON  mdl_course_categories.parent= facultad.parent
WHERE eventname='\\core\\event\\course_viewed'

SELECT 
mdl_logstore_standard_log.id,
mdl_logstore_standard_log.eventname,
mdl_logstore_standard_log.component,
mdl_logstore_standard_log.action,
mdl_logstore_standard_log.objecttable,
mdl_logstore_standard_log.objectid,
mdl_logstore_standard_log.crud,
mdl_logstore_standard_log.edulevel,
mdl_logstore_standard_log.courseid,
mdl_logstore_standard_log.other,
DATE_FORMAT(FROM_UNIXTIME(mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS timecreated,
mdl_logstore_standard_log.origin,
mdl_logstore_standard_log.ip,

mdl_user.id,
mdl_user.username,
mdl_user.idnumber,
mdl_user.firstname,
mdl_user.lastname,
mdl_user.email

FROM mdl_logstore_standard_log  
INNER JOIN mdl_user ON  mdl_logstore_standard_log.userid= mdl_user.id
WHERE eventname='\\core\\event\\user_loggedin'


!Consulta final course Course_viewed

SELECT 
mdl_logstore_standard_log.id,
mdl_logstore_standard_log.eventname,
mdl_logstore_standard_log.component,
mdl_logstore_standard_log.action,
mdl_logstore_standard_log.objecttable,
mdl_logstore_standard_log.objectid,
mdl_logstore_standard_log.crud,
mdl_logstore_standard_log.edulevel,
mdl_logstore_standard_log.ip,
mdl_logstore_standard_log.other,
DATE_FORMAT(FROM_UNIXTIME(mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS timecreated,
mdl_logstore_standard_log.origin,
mdl_logstore_standard_log.userid,

Pasas1.mdl_user.username,
Pasas1.mdl_user.idnumber,
Pasas1.mdl_user.firstname,
Pasas1.mdl_user.lastname,
Pasas1.mdl_user.email,


Pasas1.mdl_course.id,
Pasas1.mdl_course.fullname ,
Pasas1.mdl_course.shortname ,
Pasas1.mdl_course.idnumber,
Pasas1.mdl_course.startdate ,
Pasas1.mdl_course.enddate ,
Pasas1.mdl_course.category,
Pasas1.
Pasas1.
Pasas1.mdl_course_categories.name,
Pasas1.mdl_course_categories.idnumber,
Pasas1.mdl_course_categories.parent,
Pasas1.mdl_course_categories.coursecount,
Pasas1.mdl_course_categories.depth,
Pasas1.mdl_course_categories.path


FROM mdl_logstore_standard_log  
INNER JOIN mdl_course ON  mdl_logstore_standard_log.courseid= mdl_course.id   
INNER JOIN mdl_course_categories ON  mdl_course.category= mdl_course_categories.id
INNER JOIN mdl_user ON  mdl_logstore_standard_log.userid= mdl_user.id
WHERE eventname='\\core\\event\\course_viewed'




!Consulta final user_loggedin


SELECT

Pasas1.mdl_logstore_standard_log.id,
Pasas1.mdl_logstore_standard_log.eventname,
Pasas1.mdl_logstore_standard_log.component,
Pasas1.mdl_logstore_standard_log.action,
Pasas1.mdl_logstore_standard_log.objecttable,
Pasas1.mdl_logstore_standard_log.objectid,
Pasas1.mdl_logstore_standard_log.crud,
Pasas1.mdl_logstore_standard_log.edulevel,
Pasas1.mdl_logstore_standard_log.ip,
Pasas1.mdl_logstore_standard_log.other,
DATE_FORMAT(FROM_UNIXTIME(Pasas1.mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS timecreated,
Pasas1.mdl_logstore_standard_log.origin,
Pasas1.mdl_logstore_standard_log.userid,

Pasas1.mdl_user.username,
Pasas1.mdl_user.idnumber,
Pasas1.mdl_user.firstname,
Pasas1.mdl_user.lastname,
Pasas1.mdl_user.email,

Pasas1.mdl_course.id,
Pasas1.mdl_course.fullname ,
Pasas1.mdl_course.shortname ,
Pasas1.mdl_course.idnumber,
Pasas1.mdl_course.startdate ,
Pasas1.mdl_course.enddate ,
Pasas1.mdl_course.category,


Pasas1.mdl_course_categories.name,
Pasas1.mdl_course_categories.idnumber,
Pasas1.mdl_course_categories.parent,
Pasas1.mdl_course_categories.coursecount,
Pasas1.mdl_course_categories.depth,
Pasas1.mdl_course_categories.path
      
      FROM Pasas1.mdl_logstore_standard_log 
      LEFT JOIN Pasas1.mdl_user ON  Pasas1.mdl_logstore_standard_log.userid= Pasas1.mdl_user.id 
      LEFT JOIN registros.matricula ON Pasas1.mdl_user.idnumber=registros.matricula.idnumber
      LEFT JOIN Pasas1.mdl_course ON  Pasas1.mdl_course.idnumber= registros.matricula.courseid
      LEFT JOIN Pasas1.mdl_course_categories ON  Pasas1.mdl_course.category=      Pasas1.mdl_course_categories.id 

WHERE Pasas1.mdl_logstore_standard_log.eventname='\\core\\event\\user_loggedin'