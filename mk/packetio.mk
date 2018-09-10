#
# Makefile component for packet IO infrastructure
#

PIO_REQ_VARS := \
	ICP_ROOT \
	ICP_BUILD_ROOT \
	ICP_PACKETIO_DRIVER
$(call icp_check_vars,$(PIO_REQ_VARS))

PIO_SOURCES :=
PIO_INCLUDES :=
PIO_DEPENDS :=
PIO_LIBS :=

PIO_SRC_DIR := $(ICP_ROOT)/src/packetio
PIO_OBJ_DIR := $(ICP_BUILD_ROOT)/obj/packetio
PIO_LIB_DIR := $(ICP_BUILD_ROOT)/packetio

include $(PIO_SRC_DIR)/module.mk

PIO_OBJECTS := $(patsubst %, $(PIO_OBJ_DIR)/%, \
	$(patsubst %.c, %.o, $(filter %.c, $(PIO_SOURCES))))

PIO_OBJECTS += $(patsubst %, $(PIO_OBJ_DIR)/%, \
	$(patsubst %.cpp, %.o, $(filter %.cpp, $(PIO_SOURCES))))

PIO_INC_DIRS := $(PIO_SRC_DIR) $(addprefix $(PIO_SRC_DIR)/,$(PIO_INCLUDES))
PIO_CPPFLAGS := $(addprefix -I,$(PIO_INC_DIRS))
PIO_LIBRARY := packetio-$(ICP_PACKETIO_DRIVER)
PIO_TARGET := $(PIO_LIB_DIR)/lib$(PIO_LIBRARY).a

ICP_INC_DIRS += $(PIO_INC_DIRS)
ICP_LIB_DIRS += $(PIO_LIB_DIR)
ICP_LDLIBS += -Wl,--whole-archive -l$(PIO_LIBRARY) -Wl,--no-whole-archive $(PIO_LIBS)

$(info $(PIO_OBJECTS))
# Load packet-io dependencies
$(foreach DEP,$(PIO_DEPENDS),$(eval include $(ICP_ROOT)/mk/$(DEP).mk))

###
# Load stack info; always required for now
###
#LWIP_SOURCES :=
#LWIP_INCLUDES :=

#LWIP_SRC_DIR := $(ICP_ROOT)/deps/lwip
#LWIP_OBJ_DIR := $(PIO_OBJ_DIR)/lwip

#include $(ICP_ROOT)/mk/lwip.mk

#LWIP_OBJECTS := $(patsubst %, $(LWIP_OBJ_DIR)/%, \
#	$(patsubst %.c, %.o, $(LWIP_SOURCES)))
#LWIP_CPPFLAGS := $(addprefix -I,$(addprefix $(LWIP_SRC_DIR)/,$(LWIP_INCLUDES)))
#PIO_CPPFLAGS += $(LWIP_CPPFLAGS)
#PIO_CPPFLAGS += $(addprefix -I,$(DPDK_INC_DIR))

$(LWIP_OBJ_DIR)/%.o: $(LWIP_SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(strip $(ICP_CC) -o $@ -c $(PIO_CPPFLAGS) $(LWIP_CPPFLAGS) $(ICP_CPPFLAGS) $(ICP_COPTS) $<)

# Pull in object dependencies, maybe
-include $(PIO_OBJECTS:.o=.d)
#-include $(LWIP_OBJECTS:.o=.d)

###
# Build rules
###
$(PIO_OBJECTS): $(DPDK_TARGET)

$(PIO_OBJ_DIR)/%.o: $(PIO_SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(strip $(ICP_CC) -o $@ -c $(PIO_CPPFLAGS) $(ICP_CPPFLAGS) $(ICP_CFLAGS) $(ICP_COPTS) $<)

$(PIO_OBJ_DIR)/%.o: $(PIO_SRC_DIR)/%.cpp
	@mkdir -p $(dir $@)
	$(strip $(ICP_CXX) -o $@ -c $(PIO_CPPFLAGS) $(ICP_CPPFLAGS) $(ICP_CXXFLAGS) $(ICP_COPTS) $<)

$(PIO_TARGET): $(PIO_OBJECTS) $(LWIP_OBJECTS)
	@mkdir -p $(dir $@)
	$(strip $(ICP_AR) $(ICP_ARFLAGS) $@ $(PIO_OBJECTS) $(LWIP_OBJECTS))

.PHONY: packetio
packetio: $(PIO_TARGET)

.PHONY: clean_packetio
clean_packetio:
	@rm -rf $(PIO_OBJ_DIR) $(PIO_LIB_DIR) $(PIO_SRC_DIR)/lwip
clean: clean_packetio
