package com.bitwyre;
import org.javatuples.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Pair<String, Integer> pair = Pair.with("Sajal", 12);
        System.out.println( "Hello World!" );
        System.out.println(pair);
    }
}
