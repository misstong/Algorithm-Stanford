import edu.duke.*;
import java.util.*;
/**
 * Write a description of Twosum here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Twosum {
    public void twosum(){
        FileResource f=new FileResource("D:\\ThunderDownload\\stanford\\2\\sum2.txt");
        ArrayList<Long> a=new ArrayList<Long>();
        HashSet<Long> set=new HashSet<Long>();
        for(String s:f.words()){
            a.add(Long.parseLong(s));
            set.add(Long.parseLong(s));
        }
        //Collections.sort(a);
        /*for(int i:a){
            if(binarySearch(a,i))
                System.out.println(i+" exist");
        }
        /*if(binarySearch(a,100)){
            System.out.println("exist");
        }*/
        int count=0;
        //System.out.println(a.size());
        for(long t=-10000;t<10001;t++){
            
            for(long i:a){
                if(t-i!=i&&set.contains(t-i))
                {
                    System.out.println(i+" "+(t-i)+"="+t);
                    count++;
                    break;
                }
            }
        }
        System.out.println(count);
        
    }
    public boolean binarySearch(ArrayList<Long> a,long i){
        int size=a.size();
        int low=0,high=size-1,middle=(low+high)/2;
        while(low<=high){
            if(a.get(middle)==i)
                return true;
            else if(a.get(middle)<i)
                low=middle+1;
            else
                high=middle-1;
            middle=(low+high)/2;
        }
        return false;
        
    }
}
