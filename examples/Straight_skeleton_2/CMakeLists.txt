set(Prefix StraightSkeleton2)
__cgal_include_package(Straight_skeleton_2)
__cgal_include_package(Polygon)

set(LIBS )
set(INCS )
__add_real_target(${Prefix}_Show_straight_skeleton exe
			SOURCE Show_straight_skeleton.cpp 
			INC ${INCS} ${LIBS})