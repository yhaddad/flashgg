Jet Validation Studies
======================


###Comments on the ```PFCHS0```

CHS uses normally the vertex 0 as  a default, this is what we call ```PFCHS0```.

* The configuration files to run CHS(PV0)
```python
process.pfCHS0 = cms.EDFilter("CandPtrSelector",
	                           src = cms.InputTag("packedPFCandidates"),
							   cut = cms.string("fromPV"))
```

* The ```CandPtrSelector``` is a process to make a selections on the candidates. In this case we select the PF candidates having a primary vertex (``` fromPV ```).

* Other selectors (or filters) are summarised in the following commands in order to select muons or electrons. The command to select object following a certain criterion is simple. Example :
```python
process.selectedMuons = cms.EDFilter("CandPtrSelector", 
                                     src = cms.InputTag("slimmedMuons"), 
                                     cut = cms.string(''))
```
 
* The previously selected muons and electrons are removed from the input collection of the CHS. This done my calling the ```CandPtrProjector``` ED producer and vetoing the selected muons and electrons. **Why are we doing that ?** we want to keep only charged hadrons for the subtractions.

**PFCHSLeg**

The CHS using the legacy vertex is a proper code written in the flashgg framework ([CHSLegacyVertexCandidateProducer.cc](flashgg/MicroAODProducers/plugins/CHSLegacyVertexCandidateProducer.cc)) 


**Pile Up Jet Identification ```PUJID```**

This method is based on tagging the jets which are more likely issued from pileup.






NOTES
=====
* [] [WorkBookMiniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD)
* NEW for 72x : n-subjettiness variables ```tau1```, ```tau2```, and ```tau3```, available as userFloats with labels ```NjettinessAK8:tau1```, ```NjettinessAK8:tau2```, and ```NjettinessAK8:tau3```
* 
