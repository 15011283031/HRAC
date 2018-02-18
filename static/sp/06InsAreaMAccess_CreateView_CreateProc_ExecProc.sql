create view [dbo].[S_SYS_INSAREAMACCESS] AS
With extendMain as (
	Select * From PAYORGBUSINESSDATA 
		Where Groupid = ( 
			Select Groupid From Payextenddatagroup 
				where isdeleted=0 
				and GROUPNAME='更新缴纳地区授权'
		) 
)
,extendDetail AS (
	select * from PAYORGBUSINESSDATADETAIL 
		where itemid in ( 
			Select ITEMID From Payextenddatagroupitem 
				Where Groupid = ( 
					Select Groupid From Payextenddatagroup 
						where isdeleted=0 
						and GROUPNAME='更新缴纳地区授权'
				) 
				AND ITEMNAME in (
					Select ITEMNAME From Payextenddatagroupitem 
						Where Groupid = ( 
							Select Groupid From Payextenddatagroup 
								where isdeleted=0 
								and GROUPNAME='更新缴纳地区授权'
						)
				)
		)
)

select detail1.ITEMVALUE 缴纳地区,detail2.ITEMVALUE 授权账户 from extendMain
	left join extendDetail detail1 on extendMain.DATAID=detail1.DATAID and detail1.ITEMID = (Select ITEMID From Payextenddatagroupitem Where Groupid = ( Select Groupid From Payextenddatagroup where isdeleted=0 and GROUPNAME='更新缴纳地区授权') AND ITEMNAME='缴纳地区')
	left join extendDetail detail2 on extendMain.DATAID=detail2.DATAID and detail2.ITEMID = (Select ITEMID From Payextenddatagroupitem Where Groupid = ( Select Groupid From Payextenddatagroup where isdeleted=0 and GROUPNAME='更新缴纳地区授权') AND ITEMNAME='授权账户')

GO


CREATE PROC usp_UpadateInsAreaMAceess as
begin
	DELETE --SELECT *
	FROM PAYINSUREAREAMACCESS WHERE BUSINESSUNITID = '0' AND USERID <> 'sa'
	AND AREAID IN (SELECT AREAID FROM PAYINSUREAREA WHERE AREANAME IN 
		(SELECT DISTINCT 缴纳地区 FROM S_SYS_INSAREAMACCESS));

	INSERT INTO PAYINSUREAREAMACCESS(USERID,AREAID,MTYPE,BUSINESSUNITID) 
	SELECT U.id,A.AREAID,1 MTYPE,'0' BUSINESSUNITID FROM S_SYS_INSAREAMACCESS M
		join PAYINSUREAREA A ON A.BUSINESSUNITID = '0' AND M.缴纳地区=A.AREANAME
		join gcore.om_user U ON U.muid = '0' AND U.account = M.授权账户;

END

GO

exec dbo.usp_UpadateInsAreaMAceess

GO


