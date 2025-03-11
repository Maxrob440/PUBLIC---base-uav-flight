import geopandas as gpd

class Shp_Opener:
    def __init__(self,shp_path,trans_path):
        self.path = shp_path
        self.plots = gpd.read_file(shp_path)
        self.trans_path = trans_path

    def get_trans(self):
        trans_points = []
        points = gpd.read_file(self.trans_path)
        for point in points['geometry']:
            coords = list(point.coords)#
            for cood in coords:
                trans_points.append([cood[0],cood[1]])
            # trans_points.append([coords[0][0],coords[0][1]])
        return trans_points

    def get_points(self):        
        line_points = []
        plots = gpd.read_file(self.path)
        for points in plots['geometry']:
            x=points.x
            y=points.y
            # print(x,y)
            # print(z)
            line_points.append([x,y])
        return line_points
if __name__ == '__main__':
    main = Shp_Opener('Data/Data/M345/Additional_Data/1_M345_plots.shp','Data/Data/M345/Additional_Data/2_transects_M345.shp')
    print(len(main.get_trans()))
    print(len(main.get_points()))