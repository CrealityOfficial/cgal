#ifndef CGAL_SPYCC_MACROS_H
#define CGAL_SPYCC_MACROS_H

#if USE_SPYCC
#include "ccglobal/spycc.h"
#else
#define ANALYSIS_START(x)
#define ANALYSIS_TICK(x)
#define ANALYSIS_DUMP(x)
#endif

#endif // CGAL_SPYCC_MACROS_H
