import org.apache.log4j.{Level, Logger}
object Test{
    def main() {
        sc.setLogLevel("WARN")
        //Logger.getLogger("org.apache.spark").setLevel(Level.WARN)
        val log = Logger.getLogger(this.getClass)
        log.warn("this is a warn")
        println("test for david")
    }
}
Test.main()
