import sys
import getopt
from trconfig import Configuration
from trcalc import TrajectoryCalc
from trcalc import ConstV2TrCalc
from trcalc import LinearV2TrCalc
from trcalc import TrigonometricV2TrCalc

def main(argv):

    help = "\nOption\tLongoption\tDescription\n\n-a\t--algorithm\tSet an Algorithm for steering angle calculation (constant,linear,trigonometric)\n-l\t--lenght\tSet length of Vehicle\n-s\t--steeringangle\tSet the Steering angle. Works only with constant steering angle algorithm\n-v\t--velocity\tSet the velocity at the rear angle\n-d\t--timedelta\tSet the time between each step. A small value approximates the path better, but needs more calculations\n-t\t--timeframe\tSet the total time of the simulation\n"
    
    try:
        opts, args = getopt.getopt(argv,"ha:l:s:v:d:t:",["algorithm=","length=","steeringangle=","velocity=","timedelta=","timeframe="])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
        
        algorithm = ""
        length = 1
        steeringangle = 0
        velocity = 1
        timedelta = 0.1
        timeframe = 1
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()
        elif opt in ("-a","--algorithm"):
            algorithm = arg
        elif opt in ("-l","--lenght"):
            length = float(arg)
        elif opt in ("-s","--steeringangle"):
            steeringangle = float(arg)
        elif opt in ("-v","--velocity"):
            velocity = float(arg)
        elif opt in ("-d","--timedelta"):
            timedelta = float(arg)
        elif opt in ("-t","--timeframe"):
            timeframe = float(arg)
            
    sc = Configuration();
    
    if algorithm == "constant":
        if timedelta <= timeframe:
            tr = ConstV2TrCalc(sc,length,velocity,timedelta,timeframe,steeringangle)
            
        else:
            print("Timedelta must be smaller than timeframe")
            sys.exit()
         
    elif algorithm == "linear":
        if timedelta <= timeframe:
            tr = LinearV2TrCalc(sc,length,velocity,timedelta,timeframe)
        else:
            print("Timedelta must be smaller than timeframe")
            sys.exit()
    
    elif algorithm == "trigonometric":
        if timedelta <= timeframe:
            tr = TrigonometricV2TrCalc(sc,length,velocity,timedelta,timeframe)
        else:
            print("Timedelta must be smaller than timeframe")
            sys.exit()
    
    else:
        print("Please specify which algorithm to use")
        sys.exit()
        
    tr.plotTrajectory()
        
    
        
        
if __name__ == "__main__":
    main(sys.argv[1:])
