import java.io.*; 
import java.sql.*; 
public class jdbcc 
{ 
public static void main(String args[]) throws IOException 
{ 
try 
{ 
    Class.forName("sun.jdbc.odbc.JdbcOdbcDriver"); 
    Connection cn=DriverManager.getConnection("jdbc:odbc:mydsn"); 
    System.out.println("Connected..."); 
    Statement st=cn.createStatement(); 
    st.executeUpdate(""); 
    ResultSet rs=st.executeQuery("select empname from Employee where MAX(SALARY)");
 while(rs.next()) 
 { 
 System.out.print(rs.getInt(1)+rs.getString(2)+"\t"+rs.getInt(3)+"\t"+rs.getInt(4)+"\t"+r
s.getString(5)+"\t"); 
 System.out.println(); 
 } 
 cn.close(); 
} 
catch(Exception e) 
{ 
 System.out.println(e); 
} } } 