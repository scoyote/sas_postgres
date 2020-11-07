#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


SAS_config_names=['sas94']

SAS_config_options = {'lock_down': False,
                      'verbose'  : True,
                      'prompt'   : True
                     }

SAS_output_options = {'output' : 'html5'}       # not required unless changing any of the default


sas94 = {'java'      : '/usr/bin/java',
            'iomhost'   : 'sas-94',
            'iomport'   : 8591,
            }           
