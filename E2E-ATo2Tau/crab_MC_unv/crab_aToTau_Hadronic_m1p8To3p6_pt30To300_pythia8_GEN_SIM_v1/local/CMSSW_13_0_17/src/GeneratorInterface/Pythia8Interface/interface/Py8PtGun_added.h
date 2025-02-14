#ifndef Py8PtGunV3_H
#define Py8PtGunV3_H

#include "GeneratorInterface/Core/interface/GeneratorFilter.h"
#include "GeneratorInterface/ExternalDecays/interface/ExternalDecayDriver.h"
#include "GeneratorInterface/Pythia8Interface/interface/Py8GunBase.h"
#include <numeric>

inline int sum(std::vector <int> dist) {
    return std::accumulate(dist.begin(), dist.end(), 0);
}

inline double max_element(std::vector <double> dist) {
    double max = 0;
    int s = dist.size();
    for (int i = 0; i < s; i++) {
        double el = dist[i];
        if (max < el){max = el;}
    }
    return max;
}

inline std::vector <double> get_inverse_pdf(std::vector <int> dist) {
    std::vector <double> invpdf(dist.size());
    double sum_hist = sum(dist);
    int s = dist.size();
    for (int i = 0; i < s; i++) {
        if (dist[i] != 0 ) {
            invpdf[i] = sum_hist / dist[i];
            //std::cout << "Bin " << i << " -> " << invpdf[i] << std::endl;
        }
        else {invpdf[i] = 1;}
    }
    double max_invpdf = max_element(invpdf);
    for (int i = 0; i < s; i++) {
        invpdf[i] = invpdf[i] / max_invpdf;
    }
    return invpdf;
}

inline double lookup_mass_invpdf(double mgen, std::vector <double> m_bins, std::vector <double> m_invpdf) {
    int im = 0;
    int s1 = m_bins.size();
    int s2 = m_invpdf.size();
    for (int ib = 0; ib < s1; ib++) {
        im = ib;
        if (ib + 1 >  s2 - 1) { break; }
        if (mgen <= m_bins[ib]) { break; }
    }
    return m_invpdf[im];
}

inline double lookup_pt_invpdf(double pTgen, std::vector <int> pT_bins, std::vector <double> pT_invpdf) {
    int ipt = 0;
    int s1 = pT_bins.size();
    int s2 = pT_invpdf.size();
    for (int ib = 0; ib < s1; ib++) {
        ipt = ib;
        if (ib + 1 >  s2 - 1) { break; }
        if (pTgen <= pT_bins[ib]) { break; }
    }
    return pT_invpdf[ipt];
}

inline double lookup_invpdf(double Mgen, std::vector <double> M_bins, double pTgen, std::vector <int> pT_bins, std::vector <double> invpdf) {
    unsigned int ibin = 0;
    unsigned int m1  = M_bins.size();
    unsigned int pt1 = pT_bins.size();
    unsigned int inv = invpdf.size();
    bool found_mass = false;
    bool found_end  = false;
    for (unsigned int ibx = 0; ibx < m1; ibx++) {
        if (found_mass || found_end) { break; }
        for (unsigned int iby = 0; iby < pt1; iby++) {
            ibin = (ibx*pt1)+ iby;
            if ( ((ibx*pt1) + iby + 1) >  (inv - 1) ) {
                found_end = true;
                break;
            }
            if ( (Mgen  <= M_bins[ibx]) && (pTgen <= pT_bins[iby]) ) {
                found_mass = true;
                break;
            }
        }
    }
    return invpdf[ibin];
}

inline double get_rand_el(std::vector <int> dist) {
    int randomIndex = rand() % dist.size();
      return dist[randomIndex];
}
#endif // Py8PtGunV3_H
