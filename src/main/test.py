import os
import stdata
import config
import math
import flights
import signal_analysis


#  Test dir
main_dir = os.path.dirname(os.path.abspath(__file__))
res_dir = os.path.join(main_dir, '../resources')
test_dir = os.path.join(main_dir, '../test')
stat_dir = os.path.join(res_dir, './statistics')
twist_dir = os.path.join(res_dir, './twist')

os.makedirs(test_dir, exist_ok=True)
os.makedirs(stat_dir, exist_ok=True)
os.makedirs(twist_dir, exist_ok=True)


# Test Aircraft Data
ac_data_obj = config.Config()
test_config_obj_path = os.path.join(test_dir, 'test_config_obj.txt')

file = open(test_config_obj_path, 'w')

file.write('Config reading test\n')

file.write('\n')

file.write('Fatigue Data\n')

file.write('Airborne Time: {:8d}\n'.format(ac_data_obj.airborne_time))
file.write('Flight Time: {:8d}\n'.format(ac_data_obj.flight_time))
file.write('Blocks: {:8d}\n'.format(ac_data_obj.nblocks))
file.write('Flights per Block: {:8d}\n'.format(ac_data_obj.flts_per_block))
file.write('Flight Types: {:8d}\n'.format(ac_data_obj.flight_types))
file.write('Range: {:10.3f}\n'.format(ac_data_obj.flight_range))


file.close()

# Test write th with tf
flights_obj = flights.Flights(ac_data_obj.flt_path)
flight_obj_th_tf = flights_obj.flight_to_th(ac_data_obj.flts_per_block, ac_data_obj.block, ac_data_obj.logs, 0, 1, ac_data_obj.tfpath)
flight_th = signal_analysis.Th("Wing Root Bending Moment", flight_obj_th_tf)




# Test Flight Statistics - Gust

gust_st_path = os.path.join(stat_dir, 'ac23-13a_gust.txt')
twist_path = os.path.join(twist_dir, 'twist_gust.txt')

multiplier = float(ac_data_obj.nblocks) * float(ac_data_obj.flight_range) * float(ac_data_obj.flts_per_block)
 
gust_st_obj = stdata.Flight_statistics(gust_st_path, \
                                       ac_data_obj.profile.time, \
                                       ac_data_obj.airborne_time, \
                                       multiplier, \
                                       twist_path, \
                                       ac_data_obj.nblocks)
    
    
test_gust_st_obj_path = os.path.join(test_dir, 'test_gust_st_obj.txt')

file = open(test_gust_st_obj_path, 'w')

file.write('Statistics reading test\n')

file.write('Multiplying Factor: {:10.2f}\n'.format(multiplier))

file.write('lfg+           exc        lfg-            exc     -   Original Statistic\n')

        
for i in range(int(gust_st_obj.nps)):
            
    formatted_data = "{:8.3f}  {:16.2f}  {:8.3f}  {:16.2f}\n".format(gust_st_obj.statistics[i, 0], \
                                                                     gust_st_obj.statistics[i, 1], \
                                                                     gust_st_obj.statistics[i, 3], \
                                                                     gust_st_obj.statistics[i, 4])                                               
    file.write(formatted_data)


file.write('lfg+           exc        lfg-            exc     -   Log Statistic\n')

        
for i in range(int(gust_st_obj.nps)):
            
    formatted_data = "{:8.3f}  {:16.6f}  {:8.3f}  {:16.6f}\n".format(gust_st_obj.statistics[i, 0], \
                                                                     gust_st_obj.statistics[i, 2], \
                                                                     gust_st_obj.statistics[i, 3], \
                                                                     gust_st_obj.statistics[i, 5])                                               
    file.write(formatted_data)

file.write('Level   Exc             Exc(log)        Load1       Load2\n')

    
for i in range(10):
    
    level = i + 1
    
    formatted_data = "{:8d} {:16.3f} {:16.3f} {:10.4f} {:10.4f}\n".format(level, \
                                                                          gust_st_obj.discrete.exc[i], \
                                                                          math.log10(gust_st_obj.discrete.exc[i]), \
                                                                          gust_st_obj.levels[i, 0], \
                                                                          gust_st_obj.levels[i, 1])

    file.write(formatted_data)

        
file.close()

gust_graph_path = os.path.join(test_dir, 'test_gust.png')

gust_st_obj.print_discrete_load_levels_graph(gust_graph_path, "Gust")

# Test Flight Statistics - Maneuver

maneuver_st_path = os.path.join(stat_dir, 'ac23-13a_maneuver.txt')
twist_path = os.path.join(twist_dir, 'twist_maneuver.txt')

multiplier = float(ac_data_obj.nblocks) * float(ac_data_obj.flight_range) * float(ac_data_obj.flts_per_block)
 
maneuver_st_obj = stdata.Flight_statistics(maneuver_st_path, \
                                       ac_data_obj.profile.time, \
                                       ac_data_obj.airborne_time, \
                                       multiplier, \
                                       twist_path, \
                                       ac_data_obj.nblocks)
    
    
test_maneuver_st_obj_path = os.path.join(test_dir, 'test_man_st_obj.txt')

file = open(test_maneuver_st_obj_path, 'w')

file.write('Statistics reading test\n')

file.write('Multiplying Factor: {:10.2f}\n'.format(multiplier))

file.write('lfg+           exc        lfg-            exc     -   Original Statistic\n')

        
for i in range(int(maneuver_st_obj.nps)):
            
    formatted_data = "{:8.3f}  {:16.2f}  {:8.3f}  {:16.2f}\n".format(maneuver_st_obj.statistics[i, 0], \
                                                                     maneuver_st_obj.statistics[i, 1], \
                                                                     maneuver_st_obj.statistics[i, 3], \
                                                                     maneuver_st_obj.statistics[i, 4])                                               
    file.write(formatted_data)


file.write('lfg+           exc        lfg-            exc     -   Log Statistic\n')

        
for i in range(int(maneuver_st_obj.nps)):
            
    formatted_data = "{:8.3f}  {:16.6f}  {:8.3f}  {:16.6f}\n".format(maneuver_st_obj.statistics[i, 0], \
                                                                     maneuver_st_obj.statistics[i, 2], \
                                                                     maneuver_st_obj.statistics[i, 3], \
                                                                     maneuver_st_obj.statistics[i, 5])                                               
    file.write(formatted_data)

file.write('Level   Exc             Exc(log)        Load1       Load2\n')

    
for i in range(10):
    
    level = i + 1
    
    formatted_data = "{:8d} {:16.3f} {:16.3f} {:10.4f} {:10.4f}\n".format(level, \
                                                                          maneuver_st_obj.discrete.exc[i], \
                                                                          math.log10(maneuver_st_obj.discrete.exc[i]), \
                                                                          maneuver_st_obj.levels[i, 0], \
                                                                          maneuver_st_obj.levels[i, 1])

    file.write(formatted_data)

        
file.close()

maneuver_graph_path = os.path.join(test_dir, 'test_maneuver.png')

maneuver_st_obj.print_discrete_load_levels_graph(maneuver_graph_path, "Maneuver")


