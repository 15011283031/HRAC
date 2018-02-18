create view [dbo].[S_SYS_INSAREAMACCESS] AS
With extendMain as (
	Select * From PAYORGBUSINESSDATA 
		Where Groupid = ( 
			Select Groupid From Payextenddatagroup 
				where isdeleted=0 
				and GROUPNAME='���½��ɵ�����Ȩ'
		) 
)
,extendDetail AS (
	select * from PAYORGBUSINESSDATADETAIL 
		where itemid in ( 
			Select ITEMID From Payextenddatagroupitem 
				Where Groupid = ( 
					Select Groupid From Payextenddatagroup 
						where isdeleted=0 
						and GROUPNAME='���½��ɵ�����Ȩ'
				) 
				AND ITEMNAME in (
					Select ITEMNAME From Payextenddatagroupitem 
						Where Groupid = ( 
							Select Groupid From Payextenddatagroup 
								where isdeleted=0 
								and GROUPNAME='���½��ɵ�����Ȩ'
						)
				)
		)
)

select detail1.ITEMVALUE ���ɵ���,detail2.ITEMVALUE ��Ȩ�˻� from extendMain
	left join extendDetail detail1 on extendMain.DATAID=detail1.DATAID and detail1.ITEMID = (Select ITEMID From Payextenddatagroupitem Where Groupid = ( Select Groupid From Payextenddatagroup where isdeleted=0 and GROUPNAME='���½��ɵ�����Ȩ') AND ITEMNAME='���ɵ���')
	left join extendDetail detail2 on extendMain.DATAID=detail2.DATAID and detail2.ITEMID = (Select ITEMID From Payextenddatagroupitem Where Groupid = ( Select Groupid From Payextenddatagroup where isdeleted=0 and GROUPNAME='���½��ɵ�����Ȩ') AND ITEMNAME='��Ȩ�˻�')

GO


CREATE PROC usp_UpadateInsAreaMAceess as
begin
	DELETE --SELECT *
	FROM PAYINSUREAREAMACCESS WHERE BUSINESSUNITID = '0' AND USERID <> 'sa'
	AND AREAID IN (SELECT AREAID FROM PAYINSUREAREA WHERE AREANAME IN 
		(SELECT DISTINCT ���ɵ��� FROM S_SYS_INSAREAMACCESS));

	INSERT INTO PAYINSUREAREAMACCESS(USERID,AREAID,MTYPE,BUSINESSUNITID) 
	SELECT U.id,A.AREAID,1 MTYPE,'0' BUSINESSUNITID FROM S_SYS_INSAREAMACCESS M
		join PAYINSUREAREA A ON A.BUSINESSUNITID = '0' AND M.���ɵ���=A.AREANAME
		join gcore.om_user U ON U.muid = '0' AND U.account = M.��Ȩ�˻�;

END

GO

exec dbo.usp_UpadateInsAreaMAceess

GO


